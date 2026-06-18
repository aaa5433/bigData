import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="제주 아쿠아플라넷 관람객 분석", layout="wide")

st.title("🐬 제주 아쿠아플라넷 관람객 분석")

# 데이터 불러오기

df = pd.read_excel("./data/아쿠아플라넷_방문객_데이터_3000건.xlsx")

# 데이터 미리보기

st.subheader("데이터 미리보기")
st.dataframe(df.head())

# KPI

col1, col2, col3 = st.columns(3)

with col1:
st.metric("총 관람객 수", len(df))

with col2:
st.metric("평균 관람시간", f"{df['관람시간(분)'].mean():.1f}분")

with col3:
st.metric("평균 결제금액", f"{df['결제금액(원)'].mean():,.0f}원")

# 성별 관람객 수

st.subheader("성별 관람객 수")

gender_count = df['성별'].value_counts()

fig, ax = plt.subplots()
gender_count.plot(kind='bar', ax=ax)
ax.set_title('성별 관람객 수')
st.pyplot(fig)

# 연령대별 관람객 수

st.subheader("연령대별 관람객 수")

age_count = df['연령대'].value_counts()

fig, ax = plt.subplots()
age_count.plot(kind='bar', ax=ax)
ax.set_title('연령대별 관람객 수')
st.pyplot(fig)

# 입장권 종류별 판매 수

st.subheader("입장권 종류별 판매 수")

ticket_count = df['입장권'].value_counts()

fig, ax = plt.subplots()
ticket_count.plot(kind='bar', ax=ax)
ax.set_title('입장권 종류별 판매 수')
st.pyplot(fig)

# 기념품 구매 비율

st.subheader("기념품 구매 비율")

souvenir_count = df['기념품구매'].value_counts()

fig, ax = plt.subplots()
ax.pie(
souvenir_count,
labels=souvenir_count.index,
autopct='%1.1f%%'
)
ax.set_title('기념품 구매 비율')
st.pyplot(fig)

# 지역별 방문객 수

st.subheader("지역별 방문객 수")

region_count = df['지역'].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
region_count.plot(kind='bar', ax=ax)
ax.set_title('지역별 방문객 수')
st.pyplot(fig)
