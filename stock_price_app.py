import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

### View the stock **closing price** and **volume** of Apple!

""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2011-3-21', end=
'2021-3-21')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)