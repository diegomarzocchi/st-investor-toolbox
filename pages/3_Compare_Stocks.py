import streamlit as st
import yfinance as yf
import plotly.express as px

# Function to get historical stock data
def compare_stocks(tickers, period):
    """
    Compare the performance of multiple stocks over a specified period.

    Parameters:
    - tickers (str): Space-separated stock ticker symbols.
    - period (str): Historical data period.

    Returns:
    - pd.Series: Normalized stock prices for comparison.
    """

    df = yf.download(input_tickers, period=selected_period)
    df = df.Close
    df_normalized = (df / df.iloc[0] - 1) * 100

    return df_normalized

# Create the user interface with Streamlit
st.set_page_config(
    page_title="Investor Toolbox",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.title("Compare Stocks")
st.write(
    "This function allows you to retrieve compare stocks performance."
)

# Get user-input values
col1, col2 = st.columns(2)
with col1:
    ticker1 = st.text_input("Ticker 1:", placeholder="e.g. AAPL")
    ticker2 = st.text_input("Ticker 2:", placeholder="e.g. TSLA")
with col2:
    ticker3 = st.text_input("Ticker 3:", placeholder="e.g. KO")
    ticker4 = st.text_input("Ticker 4:", placeholder="e.g. SPY")
input_tickers = ticker1 + " " + ticker2 + " " + ticker3 + " " + ticker4

period_options = ["7d", "15d", "1mo", "2mo", "3mo", "6mo", "1y", "2y", "3y", "5y", "10y"]
selected_period = st.selectbox("Select Period:", period_options)

# Button to get historical stock price
if st.button("Compare Stocks"):
    # Use st.spinner to show a spinner while the function is executing
    with st.spinner("Fetching data..."):
        # Call the function to get the stock price
        df_normalized = compare_stocks(input_tickers, selected_period)

        # Show the results
        fig = px.line(df_normalized)

        # Additional chart layout settings
        fig.update_layout(title_text="Comparative Percent Performance")
        fig.update_yaxes(title="Percentage change")

        # Show the results
        st.plotly_chart(fig)
