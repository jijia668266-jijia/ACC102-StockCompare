# StockCompare: Interactive Global Top 50 Stocks Analysis Tool

## 📋 Project Overview
An interactive Streamlit web app that helps retail investors and finance students quickly compare performance, risk, and return of major global stocks.

**Target User**: Retail investors and finance students.

**Analytical Problem**: How can users easily compare multiple stocks’ price trends, cumulative returns, volatility, and risk-adjusted performance? 

## 📊 Dataset
- **Name**: Global Top 50 Stocks Historical Data (2006–2026)
- **Source**: [Kaggle - Global Top 50 Stocks Historical Data](https://www.kaggle.com/datasets/ibrahimshahrukh/top-50-companies-dataset)
- **Access Date**: 22 April 2026
- **File**: `top_companies_20y_daily_combined.csv` (≈26MB)

**Note**: Due to GitHub file size limit, the CSV file is **not included** in this repository.  
Please download the dataset from the Kaggle link above and place it in the root folder as `top_companies_20y_daily_combined.csv` before running the app.

## 🚀 How to Run Locally
1. Clone or download this repository
2. Download the dataset from Kaggle and place it in the project root folder
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the app:
   streamlit run app.py

✨ Main Features

Multi-stock selection (50 global top companies)
Custom date range filter
Price trend & cumulative return charts
Risk-return scatter plot
Key metrics table (Sharpe Ratio, volatility, etc.)

📁 Project Structure

app.py – Main Streamlit application
stock_analysis_notebook.ipynb – Complete Python analysis workflow
requirements.txt – Python dependencies
figures/ – Saved visualization charts
top_companies_20y_daily_combined.csv – Dataset (download from Kaggle)

🔍 Key Insights
See stock_analysis_notebook.ipynb for detailed analysis and visualizations.

**Author**: Ji Jia  
**Module**: ACC102 Mini Assignment (Track 4 – Interactive Data Analysis Tool) 
