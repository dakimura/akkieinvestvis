import streamlit as st
import pandas as pd

st.title('FX investing performance')
st.markdown('by [@akkie30](https://twitter.com/akkie30)')
st.image("https://3.bp.blogspot.com/-q3fsc28YHhA/WkR92wRCAZI/AAAAAAABJVo/7R3S9tpX2W8VmcXV40c0NOCZ1Ch2bVgrACLcBGAs/s550/kabu_chart_man_happy.png")
st.info("2023年7月に500万円で始めたFX投資の成績を可視化する。投資戦略、投資対象通貨ペアは秘密...")

df = pd.read_csv("data/performance.csv", parse_dates=["Date"], index_col=0)

st.metric(label="総資産", value="¥{:,}".format(int(df.iloc[-1]["Asset"])), delta="¥{:,}".format(int(df.iloc[-1]["Asset"]) - int(df.iloc[1]["Asset"])))
st.metric(label="口座清算価値", value="¥{:,}".format(int(df.iloc[-1]["LiquidationValue"])), delta="¥{:,}".format(int(df.iloc[-1]["LiquidationValue"]) - int(df["LiquidationValue"].dropna().iloc[0])))


st.text("総資産 - Asset[JPY]")
st.line_chart(df["Asset"].dropna())
st.text("口座清算価値 - Liquidation Value[JPY]")
st.line_chart(df["LiquidationValue"].dropna())
st.text("スワップ利益 - Swap Profit[JPY]")
st.line_chart(df["Swap"].dropna())
st.text("元データ - source data")
st.dataframe(df)

if __name__ == "__main__":
    # $ python -m streamlit run
    pass