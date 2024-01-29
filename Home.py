import streamlit as st

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

st.title("Investor Toolbox")
st.write('''
        This simple web app aims to provide you with basic tools to streamline financial tasks.
        Little by little we will add new tools and functionalities.
        
        The app has been created using the Streamlit framework (https://streamlit.io/), and market data is obtained using the yfinance library (https://pypi.org/project/yfinance/).
        
        If you have suggestions, tell us!
        ''')
st.link_button("Contact me!", "https://www.linkedin.com/in/diegomarzocchi", help=None, type="secondary", use_container_width=False)
