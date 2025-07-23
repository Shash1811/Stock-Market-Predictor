# 📈 Stock Market Predictor

A **Streamlit-based web app** that predicts stock prices using a trained **LSTM (Long Short-Term Memory)** model—a type of **Recurrent Neural Network (RNN)** that performs well on time-series data like stock prices.

---

## 🔍 Features

- Fetches historical stock data using the **Yahoo Finance (`yfinance`) API**.
- Predicts future stock prices using an **LSTM model** trained on previous stock performance.
- Displays interactive plots and visualizations of:
  - Closing prices
  - Moving averages (50-day & 100-day)
  - Predicted vs Actual prices
- **Investment suggestion system**: Based on a comparison between the 50-day and 100-day moving averages.
  > 📢 *Note: Investment suggestions are for educational purposes only. Please invest at your own risk.*

---

## 📸 Web App Screenshots

| Model Prediction | Moving Averages |
|------------------|-----------------|
| ![Prediction](https://github.com/user-attachments/assets/173533d1-8d8e-4bc6-8683-4f0ea529ec18) | ![MA](https://github.com/user-attachments/assets/6b975d87-f369-4771-ad56-eb211f2d95fa) |
| ![Graph](https://github.com/user-attachments/assets/2e932d85-352c-4938-ad35-a7fbe8d22626) | ![Graph2](https://github.com/user-attachments/assets/4cadd175-1cbb-4915-bab0-ee33167b8d5f) |
| ![Result](https://github.com/user-attachments/assets/5eeb2573-f526-410a-a218-33bfab004c05) | ![Result2](https://github.com/user-attachments/assets/ff0d83a8-c031-4687-9164-59555eae860a) |

---

## 📦 Technologies Used

- **Python**
- **Keras** and **TensorFlow** – for building the LSTM model
- **yfinance** – to fetch stock market data
- **scikit-learn** – for data preprocessing
- **Streamlit** – for the web interface
- **Matplotlib** – for plotting graphs

---

## 🚀 Getting Started

1. Clone the repository
2. Install required libraries from `requirements.txt`
3. Run the Streamlit app:
   ```bash
   streamlit run app.py

