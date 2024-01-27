import streamlit as st

st.set_page_config(
        page_title="Investor Toolbox",
        page_icon=":chart_with_upwards_trend:",
        layout="wide"
)

st.title("Investor Toolbox")
st.write('''
        This simple web app aims to provide you with basic tools to streamline financial tasks.
        Little by little we will add new tools and functionalities.
        
        The app has been created using the Streamlit framework (https://streamlit.io/), and market data is obtained using the yfinance library (https://pypi.org/project/yfinance/).
        
        If you have suggestions, tell us!
        ''')
