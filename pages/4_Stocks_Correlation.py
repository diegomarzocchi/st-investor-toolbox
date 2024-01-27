import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px

# Function to get historical stock data
def stocks_correlation(tickers, period):
    """
    Calculate the correlation matrix between multiple stocks.

    Parameters:
    - tickers (str): Space-separated stock ticker symbols.
    - period (str): Historical data period.

    Returns:
    - pd.DataFrame: Correlation matrix.
    """
    df = yf.download(input_tickers, period=selected_period)
    df = df.Close
    df = df.reset_index(drop=True)
    corr_matrix = df.corr(method='pearson')

    return corr_matrix

# Create the user interface with Streamlit
st.set_page_config(
    page_title="Investor Toolbox",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.title("Stocks Correlation")
st.write(
    "This feature allows you to explore the correlation between stocks."
)

# Get user-input values

# Create list of symbols
# URL of the web page containing symbols
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
# Selector
selector = 0

@st.cache_data
def get_symbols(url, selector):
    # Use pd.read_html to extract DataFrames directly from the web page
    symbols = pd.read_html(url)[selector]

    return symbols

symbols = get_symbols(url, selector)

tickers = st.multiselect("Select Tickers", symbols)
#tickers = st.text_input("Enter Tickers (space-separated):", placeholder="e.g. AAPL TSLA KO SPY MMM AMZN DE")
input_tickers = " ".join(map(str, tickers))

period_options = ["1mo", "2mo", "3mo", "6mo", "1y", "2y", "3y", "5y", "10y"]
selected_period = st.selectbox("Select Period:", period_options)

# Button to get historical stock price
if st.button("Stocks Correlation"):
    # Use st.spinner to show a spinner while the function is executing
    with st.spinner("Calculating the correlation..."):
        # Call the function to get the stock price
        corr_matrix = stocks_correlation(input_tickers, selected_period)

        # Show the results
        # Create a heatmap plot with Plotly Express
        fig = px.imshow(corr_matrix,
                        labels=dict(color="Correlation"),
                        x=corr_matrix.columns,
                        y=corr_matrix.columns,
                        color_continuous_scale="rdbu",
                        text_auto=True,
                        zmin=-1, zmax=1)

        # Additional chart layout settings
        fig.update_layout(width=800, height=600, title_text="Correlation Matrix")

        # Show the results
        st.plotly_chart(fig)
