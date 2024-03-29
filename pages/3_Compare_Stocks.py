import streamlit as st
import yfinance as yf
import plotly.express as px

# Function to get historical stock data
def compare_stocks(tickers, period):
    try:
        # Attempt to download historical stock data
        df = yf.download(tickers, period=period)
        df = df.Close
        # Normalize the data for comparison
        df_normalized = (df / df.iloc[0] - 1) * 100
        return df_normalized
    except:
        # Handle errors and display an error message
        st.error(f"Error fetching data.")
        return None

# Create the user interface with Streamlit
st.set_page_config(
        page_title="Investor Toolbox",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        menu_items={
                'About':
                '''
                Disclaimer:
                The information provided by this application is for informational purposes only and should not be considered as financial or investment advice. The user assumes full responsibility for any decision or action taken based on the information provided by this application.
                
                The application does not guarantee the accuracy, completeness, or timeliness of the information provided. Stock market data and any other financial information may be subject to change without notice. The user should verify the accuracy of the information before making any decisions.
                
                The use of this application is subject to acceptance of the terms and conditions set forth. The application and its developers are not responsible for losses, damages, or harm arising from the use of the provided information.
                
                It is strongly recommended that the user consult with a professional financial advisor before making investment decisions. Investing in stocks and other financial instruments carries risks, and the user should fully understand those risks before proceeding.
                '''
        }
)

st.title("Compare Stocks")
st.write(
    "This function allows you to compare the performance of multiple stocks."
)

# Get user-input values
col1, col2 = st.columns(2)
with col1:
    # User input for ticker symbols
    ticker1 = st.text_input("Symbol 1:", placeholder="e.g. AAPL")
    ticker2 = st.text_input("Symbol 2:", placeholder="e.g. TSLA")
with col2:
    ticker3 = st.text_input("Symbol 3:", placeholder="e.g. KO")
    ticker4 = st.text_input("Symbol 4:", placeholder="e.g. SPY")
input_tickers = ticker1 + " " + ticker2 + " " + ticker3 + " " + ticker4

period_options = ["7d", "15d", "1mo", "2mo", "3mo", "6mo", "1y", "2y", "3y", "5y", "10y"]
selected_period = st.selectbox("Select Period:", period_options)

# Button to get historical stock price
if st.button("Compare Stocks"):
    if not input_tickers.strip():
        # Display an error if no ticker symbols are provided
        st.error("Please enter at least one ticker symbol.")
    else:
        with st.spinner("Fetching data..."):
            # Call the function to get the stock price
            df_normalized = compare_stocks(input_tickers, selected_period)
            if df_normalized is not None:
                # Show the results if there are no errors
                fig = px.line(df_normalized)
                fig.update_layout(title_text="Comparative Percent Performance")
                fig.update_yaxes(title="Percentage change")
                st.plotly_chart(fig)
