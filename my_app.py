import streamlit as st
import pandas as pd

st.title('FX investing performance')
st.markdown('by [@akkie30](https://twitter.com/akkie30)')
df = pd.read_csv("data/performance.csv", parse_dates=["Date"], index_col=0)
st.text("Liquidation Value[JPY]")
st.line_chart(df["LiquidationValue"])
st.text("Asset[JPY]")
st.line_chart(df["Asset"])
st.text("Swap Profit[JPY]")
st.line_chart(df["Swap"])
st.text("source data")
st.dataframe(df)

if __name__ == "__main__":
    # $ python -m streamlit run
    pass