import streamlit as st
import yfinance as yf
from datetime import timedelta, datetime

# Function to get historical stock data
def get_historical_price(ticker, start_date, end_date, selected_interval):
    """
    Retrieve historical stock data for a given ticker symbol and date range.

    Parameters:
    - ticker (str): Stock ticker symbol.
    - start_date (datetime.date): Start date for historical data retrieval.
    - end_date (datetime.date): End date for historical data retrieval.
    - selected_interval (str): Time interval for stock data.

    Returns:
    - pd.DataFrame: Historical stock data.
    """

    # Download stock data for the specified date range and interval
    df_historical = yf.download(ticker, start=start_date, end=end_date, interval=selected_interval)

    # Check if the DataFrame is empty
    if df_historical.empty:
        st.error(f"Error fetching data.")

    return df_historical

# Create the user interface with Streamlit
st.set_page_config(
    page_title="Investor Toolbox",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.title("Get Historical Price")
st.write(
    "This function allows you to retrieve historical stock prices between two dates with a specific interval."
)

# Get user-input values
ticker = st.text_input("Ticker:", placeholder="e.g. AAPL")

max_date = datetime.now().date()
start_date = st.date_input("Select Start Date:", max_value=max_date)
end_date = st.date_input("Select End Date:", min_value=start_date, max_value=max_date) + timedelta(days=1)

# Calculate the difference in days between start_date and today
days_difference = (datetime.now().date() - start_date).days

# Time interval selector based on the days_difference
if days_difference < 7:
    interval_options = ["1m", "2m", "5m", "15m", "30m", "60m", "1d", "5d", "1wk", "1mo", "3mo"]
elif days_difference <= 30:
    interval_options = ["2m", "5m", "15m", "30m", "60m", "1d", "5d", "1wk", "1mo", "3mo"]
elif 30 < days_difference <= 60:
    interval_options = ["2m", "5m", "15m", "30m", "60m", "1d", "5d", "1wk", "1mo", "3mo"]
elif 60 < days_difference < 730:
    interval_options = ["60m", "1d", "5d", "1wk", "1mo", "3mo"]
else:
    interval_options = ["1d", "5d", "1wk", "1mo", "3mo"]

# Allow the user to select the interval
selected_interval = st.selectbox("Select Interval:", interval_options)

# Button to get historical stock price
if st.button("Get Historical Price"):
    # Use st.spinner to show a spinner while the function is executing
    if not ticker.strip():
        # Display an error if no ticker symbols are provided
        st.error("Please enter one ticker symbol.")
    else:
        with st.spinner("Fetching historical data..."):
            # Call the function to get the stock price
            dfhistorical = get_historical_price(ticker, start_date, end_date, selected_interval)

            # Show the results
            st.dataframe(dfhistorical)
