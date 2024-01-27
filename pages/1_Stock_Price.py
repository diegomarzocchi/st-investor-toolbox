import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta, timezone
import pytz
import tzlocal

# Function to get the closest stock price
def get_stock_price(ticker, target_datetime, timezone_str, interval):
    """
    Retrieve the closest stock price for a given date, time, and interval.

    Parameters:
    - ticker (str): Stock ticker symbol.
    - target_datetime (datetime): Target date and time for stock price retrieval.
    - timezone_str (str): Selected timezone for date and time.
    - interval (str): Time interval for stock data.

    Returns:
    - company (str): Company information.
    - market_date (str): Market date and time.
    - result (str): Result message with average price.
    """
    # Convert the target date and time to the selected time zone
    target_datetime = pytz.timezone(timezone_str).localize(target_datetime)

    # Convierte a UTC y luego quita la información de zona horaria
    target_datetime_naif = target_datetime.astimezone(timezone.utc).replace(tzinfo=None)

    # Define the date range for the query
    start_date = target_datetime - timedelta(hours=2)
    end_date = target_datetime + timedelta(hours=2)

    # Download stock data for the specified date range and interval
    df = yf.download(ticker, start=start_date, end=end_date, interval=interval)

    # Check if the DataFrame is empty
    if df.empty:
        return "No stock price available for the selected data", "", ""
        
    # Verificar si el índice tiene información de zona horaria
    dfnaif = df.copy()
    if dfnaif.index.tz is not None:
        # Si tiene información de zona horaria, convertir a None
        dfnaif.index = dfnaif.index.tz_convert(None)
    else:
        # Si no tiene información de zona horaria, localizar y luego convertir a None
        dfnaif.index = dfnaif.index.tz_localize('America/New_York').tz_convert(None)

    # Get the company name
    company_name = yf.Ticker(ticker).info['longName']

    # Find the index of the row closest to the target date
    index = dfnaif.index.get_indexer([target_datetime_naif])
    closest_datetime = dfnaif.index[index[0]]

    # Calculate the average of low and high prices
    average_price = (dfnaif.loc[closest_datetime, 'Low'] + dfnaif.loc[closest_datetime, 'High']) / 2

    # Build the description and result messages
    company = f"### Company: {company_name}"
    market_date = f"**Market date and time:** {df.index[index[0]]}"
    result = f"**Average of Low and High prices:** ***USD {average_price:.2f}***"

    return company, market_date, result

# Create the user interface with Streamlit
st.set_page_config(
    page_title="Investor Toolbox",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.title("Get Stock Price")
st.write(
    "This function allows you to retrieve stock prices for a specific date and time."
)

# Get user-input values
ticker = st.text_input("Ticker:", placeholder="e.g. APPL")

# Restrict the date selection to the last 730 days
min_date = datetime.now().date() - timedelta(days=730)
max_date = datetime.now().date()
selected_date = st.date_input("Select Date:", min_value=min_date, max_value=max_date)

# Time interval selector
def get_allowed_intervals(selected_date):
    if selected_date >= (datetime.now().date() - timedelta(days=30)):
        return ["1m", "2m", "5m", "15m", "30m", "60m"]
    elif selected_date >= (datetime.now().date() - timedelta(days=60)):
        return ["2m", "5m", "15m", "30m", "60m"]
    else:
        st.warning("Interval restricted to 60m for dates 60 to 730 days ago.")
        return ["60m"]

interval_options = get_allowed_intervals(selected_date)
selected_interval = st.selectbox("Select Interval:", interval_options)

# Adjust the time input based on the selected interval
step_seconds = int(selected_interval[:-1]) * 60
selected_time = st.time_input("Select Time:", value=None, step=step_seconds)

# Timezone
default_timezone = tzlocal.get_localzone().key
timezone_str = st.selectbox("Select Timezone:", pytz.all_timezones, index=pytz.all_timezones.index(default_timezone))

# Button to get the stock price
if st.button("Get Stock Price"):
    # Use st.spinner to show a spinner while the function is executing
    with st.spinner("Fetching data..."):
        # Call the function to get the stock price
        target_datetime = datetime.combine(selected_date, selected_time)
        company, market_date, result = get_stock_price(ticker, target_datetime, timezone_str, selected_interval)

        # Show the results
        st.markdown(company)
        st.markdown(market_date)
        st.markdown(result)
