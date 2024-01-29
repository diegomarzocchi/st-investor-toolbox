import streamlit as st
import yfinance as yf

def get_data(ticker, function):
    # Create a Ticker object for the specified stock
    ticker_obj = yf.Ticker(ticker)
    
    # Define a mapping of available functions to their corresponding yfinance methods
    function_mapping = {
        'Info': ticker_obj.info,
        'Actions': ticker_obj.actions,
        'Dividends': ticker_obj.dividends,
        'Splits': ticker_obj.splits,
        'Balance Sheet': ticker_obj.balance_sheet,
        'Quarterly Balance Sheet': ticker_obj.quarterly_balance_sheet,
        'Cashflow': ticker_obj.cashflow,
        'Quarterly Cashflow': ticker_obj.quarterly_cashflow,
        'Major Holders': ticker_obj.major_holders,
        'Institutional Holders': ticker_obj.institutional_holders,
        'Mutualfund Holders': ticker_obj.mutualfund_holders,
        'Insider Transactions': ticker_obj.insider_transactions,
        'Insider Purchases': ticker_obj.insider_purchases,
        'Insider Roster Holders': ticker_obj.insider_roster_holders,
        'Recommendations': ticker_obj.recommendations,
        'Upgrades Downgrades': ticker_obj.upgrades_downgrades,
        'Earnings Dates': ticker_obj.earnings_dates,
        'News': ticker_obj.news
    }

    # Check if the selected function is in the mapping
    if function in function_mapping:
        # Return the result of the corresponding yfinance method
        return function_mapping[function]

st.set_page_config(
    page_title="Investor Toolbox",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.title("Stock Information")
st.write(
    "This section works as a graphical interface to access general functions of the yfinance library. Allows access to different types of information about companies."
)

# Input for the stock ticker
ticker_input = st.text_input('Ticker:', placeholder="e.g. AAPL")

# Radio button to select the function
function_options = [
    'Info', 'Actions', 'Dividends', 'Splits',
    'Balance Sheet', 'Quarterly Balance Sheet', 'Cashflow', 'Quarterly Cashflow',
    'Major Holders', 'Institutional Holders', 'Mutualfund Holders',
    'Insider Transactions', 'Insider Purchases', 'Insider Roster Holders',
    'Recommendations', 'Upgrades Downgrades', 'Earnings Dates', 'News'
]

selected_function = st.selectbox('Select the function to execute:', function_options)

# Button to get data
if st.button('Execute'):
    if not ticker_input.strip():
        # Display an error if no ticker symbol are provided
        st.error("Please enter one ticker symbol.")
    else:
        # Use st.spinner to show a spinner while the function is executing
        with st.spinner("Fetching data..."):
            data = get_data(ticker_input, selected_function)
            st.subheader(f'Results for {selected_function} of {ticker_input}')
            st.write(data)
