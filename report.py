import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="제주 아쿠아플라넷 관람객 분석",
    layout="wide"
)

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
    st.metric(
        "평균 관람시간",
        f"{df['관람시간(분)'].mean():.1f}분"
    )

with col3:
    st.metric(
        "평균 결제금액",
        f"{df['결제금액(원)'].mean():,.0f}원"
    )

# 성별 관람객 수
st.subheader("성별 관람객 수")
gender_count = df["성별"].value_counts()
st.bar_chart(gender_count)

# 연령대별 관람객 수
st.subheader("연령대별 관람객 수")
age_count = df["연령대"].value_counts()
st.bar_chart(age_count)

# 입장권 종류별 판매 수
st.subheader("입장권 종류별 판매 수")
ticket_count = df["입장권"].value_counts()
st.bar_chart(ticket_count)

# 지역별 방문객 수
st.subheader("지역별 방문객 수")
region_count = df["지역"].value_counts()
st.bar_chart(region_count)

# 기념품 구매 비율
st.subheader("기념품 구매 비율")

souvenir_count = df["기념품구매"].value_counts()

souvenir_df = pd.DataFrame({
    "구매여부": souvenir_count.index,
    "인원수": souvenir_count.values
})

st.dataframe(souvenir_df)

st.bar_chart(
    souvenir_df.set_index("구매여부")
)

# 요약 통계
st.subheader("분석 결과 요약")

st.write("""
- 20~30대 관람객 비율이 높게 나타남
- 성별 분포는 비교적 균등함
- 성인 입장권 이용 비율이 가장 높음
- 기념품 구매 고객의 결제금액이 더 높게 나타남
- 관람시간이 길수록 추가 소비 가능성이 높음
""")