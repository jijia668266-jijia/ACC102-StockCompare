import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

st.set_page_config(page_title="StockCompare", page_icon="📈", layout="wide")

st.title("📈 StockCompare: Interactive Global Top 50 Stocks Tool")
st.markdown("**Helping retail investors and finance students compare performance, risk and return**")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('top_companies_20y_daily_combined.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by=['Ticker', 'Date']).reset_index(drop=True)
    df['Daily_Return'] = df.groupby('Ticker')['Adj Close'].pct_change()
    df['Cumulative_Return'] = df.groupby('Ticker')['Adj Close'].transform(lambda x: x / x.iloc[0])
    df['MA20'] = df.groupby('Ticker')['Adj Close'].transform(lambda x: x.rolling(window=20).mean())
    df['Volatility_30'] = df.groupby('Ticker')['Daily_Return'].transform(lambda x: x.rolling(window=30).std())
    df['Annualized_Volatility'] = df['Volatility_30'] * np.sqrt(252)
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filter Options")
all_tickers = sorted(df['Ticker'].unique())
selected_tickers = st.sidebar.multiselect("Select Stocks", all_tickers, default=['AAPL', 'TSLA', 'NVDA', 'XOM', '0700.HK'])

min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
date_range = st.sidebar.date_input("Date Range", [datetime(2025,1,1).date(), max_date], min_value=min_date, max_value=max_date)

# Filter data
filtered_df = df[(df['Ticker'].isin(selected_tickers)) &
                 (df['Date'].dt.date >= date_range[0]) &
                 (df['Date'].dt.date <= date_range[1])]

# Main content
tab1, tab2, tab3 = st.tabs(["📊 Price & Return Trends", "📉 Risk & Return Analysis", "📋 Key Metrics"])

with tab1:
    st.subheader("Adjusted Close Price Trend")
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    for ticker in selected_tickers:
        data = filtered_df[filtered_df['Ticker'] == ticker]
        ax1.plot(data['Date'], data['Adj Close'], label=ticker)
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Adjusted Close Price")
    ax1.legend()
    st.pyplot(fig1)

    st.subheader("Cumulative Return Comparison")
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    for ticker in selected_tickers:
        data = filtered_df[filtered_df['Ticker'] == ticker]
        ax2.plot(data['Date'], data['Cumulative_Return'], label=ticker)
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Cumulative Return")
    ax2.legend()
    st.pyplot(fig2)

with tab2:
    st.subheader("Risk-Return Scatter Plot")
    summary = filtered_df.groupby('Ticker').agg({
        'Annualized_Volatility': 'last',
        'Daily_Return': 'mean'
    }).reset_index()
    summary['Annualized_Return'] = summary['Daily_Return'] * 252
   
    fig3, ax3 = plt.subplots(figsize=(10, 7))
    sns.scatterplot(data=summary, x='Annualized_Volatility', y='Annualized_Return', s=120, ax=ax3)
    for i, row in summary.iterrows():
        ax3.text(row['Annualized_Volatility'], row['Annualized_Return'], row['Ticker'], fontsize=9)
    ax3.set_xlabel("Annualized Volatility")
    ax3.set_ylabel("Annualized Return")
    st.pyplot(fig3)

with tab3:
    st.subheader("Key Performance Metrics")
    metrics = filtered_df.groupby('Ticker').agg({
        'Daily_Return': ['mean', 'std'],
        'Cumulative_Return': 'last',
        'Annualized_Volatility': 'last'
    }).round(4)
    metrics.columns = ['Avg Daily Return', 'Return Std', 'Total Cum Return', 'Annualized Vol']
    metrics['Sharpe Ratio'] = (metrics['Avg Daily Return'] - 0.04/252) / metrics['Return Std'] * np.sqrt(252)
    st.dataframe(metrics.style.format("{:.4f}"), use_container_width=True)

st.sidebar.success("App ready! Select different stocks and date ranges to explore.")

st.caption("Dataset: Global Top 50 Stocks Historical Data (2006–2026) | Accessed: 22 April 2026")
