import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta

st.markdown(
    """
    <style>
    .stApp {
        background-color: #1a1f36; /* Midnight Blue */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)




# Load the trained model
model = load_model(r'C:\Users\Shashwati B.U\OneDrive\Desktop\Stock Prediction\stock_model.keras')

st.header('📈 Stock Market Predictor')

# Date range: last 10 years
end = datetime.today()
start = end - timedelta(days=365 * 10)

# User input
stock = st.text_input("Enter stock symbol", "GOOG")

# Download data
data = yf.download(stock, start=start, end=end)

if data.empty or 'Close' not in data.columns:
    st.error("Failed to fetch data for the symbol. Please check and try again.")
    st.stop()

# Show data
st.subheader('Stock Data')
st.write(data)  # show last few rows

# Preprocessing
data_train = pd.DataFrame(data.Close[:int(len(data)*0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80):])

scaler = MinMaxScaler(feature_range=(0, 1))
pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
data_test_scaler = scaler.fit_transform(data_test)

# Moving Averages
ma_50_days = data.Close.rolling(50).mean()
ma_100_days = data.Close.rolling(100).mean()
ma_200_days = data.Close.rolling(200).mean()

# Plot MA50
st.subheader('Price vs MA50')
fig1 = plt.figure(figsize=(10, 5))
plt.plot(data.Close, label='Closing Price', color='green')
plt.plot(ma_50_days, label='MA50', color='red')
plt.legend()
st.pyplot(fig1)

# Plot MA50 & MA100
st.subheader('Price vs MA50 vs MA100')
fig2 = plt.figure(figsize=(10, 5))
plt.plot(data.Close, label='Closing Price', color='green')
plt.plot(ma_50_days, label='MA50', color='red')
plt.plot(ma_100_days, label='MA100', color='blue')
plt.legend()
st.pyplot(fig2)

# Plot MA100 & MA200
st.subheader('Price vs MA100 vs MA200')
fig3 = plt.figure(figsize=(10, 5))
plt.plot(data.Close, label='Closing Price', color='green')
plt.plot(ma_100_days, label='MA100', color='blue')
plt.plot(ma_200_days, label='MA200', color='red')
plt.legend()
st.pyplot(fig3)

# Predictions
x, y = [], []
for i in range(100, data_test_scaler.shape[0]):
    x.append(data_test_scaler[i-100:i])
    y.append(data_test_scaler[i, 0])
x = np.array(x)
y = np.array(y)

try:
    predict = model.predict(x)
except Exception as e:
    st.error(f"Prediction failed: {e}")
    st.stop()

# Inverse scaling
predict = scaler.inverse_transform(predict.reshape(-1, 1))
y = scaler.inverse_transform(y.reshape(-1, 1))

# Plot Predictions
st.subheader('Original Price vs Predicted Price')
fig4 = plt.figure(figsize=(10, 5))
plt.plot(y, label='Original Price', color='red')
plt.plot(predict, label='Predicted Price', color='green')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig4)

# Investment Suggestion
st.subheader('📊 Investment Suggestion')

try:
    latest_ma50 = ma_50_days.dropna().iloc[-1]
    latest_ma200 = ma_200_days.dropna().iloc[-1]
    
    if float(latest_ma50) > float(latest_ma200):
        st.success("✅ 50-day MA is above 200-day MA — indicates **positive trend**. You *may* consider investing.")
    else:
        st.info("⚠️ 50-day MA is below 200-day MA — market may be in **downtrend**. Be cautious.")

    st.markdown(
        "<br>🚨 **Disclaimer:** This is a simple moving average-based suggestion.<br>"
        "**Please do your own research. INVEST AT YOUR OWN RISK.**",
        unsafe_allow_html=True
    )
except Exception as e:
    st.warning(f"Could not generate suggestion: {e}")
