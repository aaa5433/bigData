import streamlit as st
import pandas as pd

st.title("제주 아쿠아플라넷 관람객 분석")

df = pd.read_excel("./data/아쿠아플라넷_방문객_데이터_3000건.xlsx")

st.write("데이터 미리보기")
st.dataframe(df.head())

st.write("연령대별 방문객 수")
st.bar_chart(df["연령대"].value_counts())