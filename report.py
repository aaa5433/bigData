import pandas as pd
import matplotlib.pyplot as plt

# 한글 깨짐 방지
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_excel('./data/아쿠아플라넷_방문객_데이터_3000건.xlsx')

# 데이터 확인
print(df.head())
print(df.info())

# 1. 성별 관람객 수
gender_count = df['성별'].value_counts()

plt.figure(figsize=(6,4))
gender_count.plot(kind='bar')
plt.title('성별 관람객 수')
plt.xlabel('성별')
plt.ylabel('인원 수')
plt.show()

# 2. 연령대별 관람객 수
age_count = df['연령대'].value_counts()

plt.figure(figsize=(8,4))
age_count.plot(kind='bar')
plt.title('연령대별 관람객 수')
plt.xlabel('연령대')
plt.ylabel('인원 수')
plt.show()

# 3. 입장권 종류별 판매 수
ticket_count = df['입장권'].value_counts()

plt.figure(figsize=(8,4))
ticket_count.plot(kind='bar')
plt.title('입장권 종류별 판매 수')
plt.xlabel('입장권')
plt.ylabel('판매 수')
plt.show()

# 4. 기념품 구매 여부 비율
souvenir_count = df['기념품구매'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    souvenir_count,
    labels=souvenir_count.index,
    autopct='%1.1f%%'
)
plt.title('기념품 구매 비율')
plt.show()

# 5. 지역별 방문객 수
region_count = df['지역'].value_counts()

plt.figure(figsize=(10,5))
region_count.plot(kind='bar')
plt.title('지역별 방문객 수')
plt.xlabel('지역')
plt.ylabel('인원 수')
plt.show()

# 6. 평균 결제금액
print("평균 결제금액:", df['결제금액(원)'].mean())

# 7. 평균 관람시간
print("평균 관람시간:", df['관람시간(분)'].mean())