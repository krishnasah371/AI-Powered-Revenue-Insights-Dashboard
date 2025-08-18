
# 📊 AI-Powered Revenue Insights Dashboard

A modern Streamlit-based dashboard that offers interactive insights into stock market trends, financial KPIs, predictions, and portfolio analysis — inspired by the S&P 500 index.

Built with Python, Plotly, and Pandas — this project simulates Azure integration via data upload and scheduling scripts.

---

## 🚀 Features

✅ Real-time stock data from Yahoo Finance  
✅ Interactive multi-tab dashboard  
✅ Closing price trends and financial statement analysis  
✅ Forecasting with Value at Risk (VaR)  
✅ Portfolio-level performance view  
✅ Azure Blob + Data Factory simulation scripts  
✅ Built using Streamlit, Pandas, Plotly, Matplotlib  

---

## 📂 Project Structure

```
AI-Revenue-Dashboard/
├── app.py                      # Main Streamlit application
├── simulate_blob_upload.py    # Simulated Azure Blob upload script
├── simulate_data_factory.py   # Simulated Data Factory ETL job
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

---

## 🧪 Simulated Azure Integration

- `simulate_blob_upload.py`  
  Saves stock data as CSV to a local `blob_storage/` folder, simulating Azure Blob.

- `simulate_data_factory.py`  
  Acts like a daily/cron job that refreshes the data — mimics Azure Data Factory.

---

## 🛠️ Setup Instructions

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit dashboard
streamlit run app.py
```

---

## 📸 Sample Dashboard Preview

*(You can add screenshots here from your running dashboard in future)*

---

## 🌐 Tech Stack

- Streamlit
- Python
- Pandas, NumPy
- Plotly, Matplotlib
- yfinance, yahoo_fin
- Simulated Azure (Blob + Data Factory)

---

## 💼 Use Case

Ideal for:
- Showcasing data engineering skills
- Streamlit portfolio projects
- Financial trend visualizations
