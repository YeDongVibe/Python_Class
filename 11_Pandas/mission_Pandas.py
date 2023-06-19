# tips.csv 파일을 read_csv 함수로 읽어드려 아래 문제를 풀어보자.

# total_bill이 20보다 큰 행들만 선택해보세요.
# sex가 'Female'인 행들만 선택해보세요.
# day가 'Sun'이고 time이 'Dinner'인 행들만 선택해보세요.
# tip이 5보다 크고 size가 3 또는 4인 행들만 선택해보세요.
# total_bill, tip, size 열만 선택해보세요.
import pandas as pd


df = pd.read_csv('C:/Ye_Dong/Python_Class/11_Pandas/tips.csv')

ex1 = df[df['total_bill'] > 20]
ex2 = df[df['sex'] == 'Female']
ex3 = df[(df['day'] == 'Sun') & (df['time'] == 'Dinner')]
ex4 = df[(df['tip'] > 5) & (df['size'].isin([3,4]))]
ex5 = df[['total_bill', 'tip','size']]

print('-'*50)
print(ex1)
print('-'*50)
print(ex2)
print('-'*50)
print(ex3)
print('-'*50)
print(ex4)
print('-'*50)
print(ex5)


# 데이터 전처리 예제
import pandas as pd

data = {'이름': ['John', 'Steve', 'Sarah', 'Ann', 'Mike'],
        '나이': [25, 32, 28, 35, 41],
        '성별': ['남', '남', '여', '여', '남'],
        '키': [175, 180, 163, 155, 190]}
df = pd.DataFrame(data)

# '학년' 열을 추가하고, 모든 행에 '3학년'이라는 값으로 채워 넣으세요.
df['학년'] = '3학년'
# '국적' 열을 추가하고, 각 행에 해당하는 사람의 국적을 채워 넣으세요.
df['국적'] = ['한국', '일본', '미국', '중국', '네덜란드']
# '성별'이 '여'인 행만 남기고 나머지 행을 삭제하세요.
df = df[df['성별'] == '여']
# '나이' 열을 기준으로 내림차순으로 행을 정렬하세요.
df = df.sort_values(by='나이', ascending=False)
# 인덱스가 2인 행을 삭제하세요.
df = df.drop(2)
# 아래 새로운 행 3개를 추가하세요.
# [{'이름': 'Alex', '나이': 22, '성별': '남', '키': 180, '학년': '2학년', '국적': '미국'}, {'이름': 'Emily', '나이': 29, '성별': '여', '키': 165, '학년': '1학년', '국적': '캐나다'}, {'이름': 'Daniel', '나이': 33, '성별': '남', '키': 175, '학년': '3학년', '국적': '호주'}]
new_rows = [{'이름': 'Alex', '나이': 22, '성별': '남', '키': 180, '학년': '2학년', '국적': '미국'}, {'이름': 'Emily', '나이': 29, '성별': '여', '키': 165, '학년': '1학년', '국적': '캐나다'}, {'이름': 'Daniel', '나이': 33, '성별': '남', '키': 175, '학년': '3학년', '국적': '호주'}]

df = df.append(new_rows, ignore_index = True)

# '이름' 열을 기준으로 오름차순으로 행을 정렬하세요.
df = df.sort_values(by='이름', ascending=True)
# '키' 열의 값을 cm에서 m로 변환하세요.
df['키'] = df['키']/100
# '성별' 열을 삭제하세요.
df = df.drop('성별', axis=1)

print(df)

#----------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {'Name': ['John', 'Mike', 'Sarah', 'Adam', 'Emily', 'Daniel', 'Olivia', 'Liam', 'Sophia', 'Ethan',
                 'Emma', 'Jacob', 'Ava', 'Mia', 'Noah', 'Charlotte', 'Harper', 'William', 'Benjamin', 'Elijah',
                 'Amelia', 'James', 'Oliver', 'Lucas', 'Mason', 'Logan', 'Alexander', 'Evelyn', 'Grace', 'Victoria'],
        'Age': np.random.randint(20, 40, 30),
        'Gender': ['Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male',
                   'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male',
                   'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female'],
        'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Seoul', 'Beijing',
                 'Moscow', 'Vienna', 'Athens', 'Cairo', 'Lisbon', 'Dublin', 'Amsterdam', 'Stockholm', 'Oslo', 'Helsinki',
                 'Copenhagen', 'Budapest', 'Prague', 'Warsaw', 'Vienna', 'Brussels', 'Luxembourg', 'Zurich', 'Geneva', 'Dubai']}
df = pd.DataFrame(data)

df['initial'] = df['Name'].str[0]
mean_age_by_initial = df.groupby('initial')['Age'].mean()
print(mean_age_by_initial)

overall_mean_age = df['Age'].mean()


plt.bar(mean_age_by_initial.index, mean_age_by_initial.values)
plt.axhline(overall_mean_age, color = 'red', linestyle = '--', label = 'overall_mean_age') #수평선 긋기

plt.xlabel('initial')
plt.ylabel('Mean Age')
plt.legend()
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt


# 데이터 파일 경로
data_path = 'C:/Ye_Dong/Python_Class/11_Pandas/일별평균대기오염도_2022.csv'

# CSV 파일 읽기
df = pd.read_csv(data_path, encoding="cp949")

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

print(df.head(20))

#----------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# 연도별 미세먼지와 초미세먼지 농도 평균 계산
df_monthly = df.resample('M', on='측정일시').mean(numeric_only=True)

# 그래프 그리기
plt.plot(df_monthly.index.month, df_monthly['미세먼지농도(㎍/㎥)'], label='PM10')
plt.plot(df_monthly.index.month, df_monthly['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Concentration')
plt.title('2022 Air Pollution Trend')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
#일별 대기오염 추이 그래프
import matplotlib.pyplot as plt

# 일별 합계 계산
df_daily = df.resample('D', on='측정일시').sum(numeric_only=True)

# 일평균 대기오염도 계산
df_daily['미세먼지농도(㎍/㎥)'] /= 24
df_daily['초미세먼지농도(㎍/㎥)'] /= 24

# 그래프 그리기
plt.plot(df_daily.index, df_daily['미세먼지농도(㎍/㎥)'], label='PM10')
plt.plot(df_daily.index, df_daily['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('2022 Air Pollution Trend')
plt.show()


#----------------------------------------------------------------------------------------------------------------------------
# 지역별 대기오염 막대 그래프
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

# 지역별 미세먼지와 초미세먼지 농도 평균 계산
df_area = df.groupby('측정소명').mean(numeric_only=True).head(20)

# 그래프 그리기
plt.bar(df_area.index, df_area['미세먼지농도(㎍/㎥)'], label='PM10')
plt.bar(df_area.index, df_area['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Area')
plt.ylabel('Concentration')
plt.title('Air Pollution by Area')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 대기오염 상자그림
import matplotlib.pyplot as plt

# 그래프 그리기
plt.boxplot([df['미세먼지농도(㎍/㎥)'], df['초미세먼지농도(㎍/㎥)']])
plt.xticks([1,2],['PM10', 'PM2.5'])
plt.ylabel('Concentration')
plt.title('Air Pollution Boxplot')
plt.show()
