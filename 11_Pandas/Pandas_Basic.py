# Pandas
# pandas는 파이썬에서 데이터 분석을 위한 라이브러리입니다.
# 표 형태의 데이터를 다루는 데 특화되어 있으며, 데이터프레임(DataFrame)이라는 자료구조를 제공합니다.
# pandas는 NumPy와 함께 사용되어 효율적인 데이터 처리가 가능합니다.

#=============================================================================================================================
# Series : 1차원 배열 형태의 자료구조 / 각 요소는 인덱스와 값으로 구성
import pandas as pd

# Series 생성
# 리스트 사용
data = pd.Series([1, 2, 3, 4])
print(data)

#----------------------------------------------------------------------------------------------------------------------------
# 문자열 인덱스 사용
data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(data)

#----------------------------------------------------------------------------------------------------------------------------
# 딕셔너리 사용
data1 = {'a': 1, 'b': 2, 'c': 3 , 'd': 4}
s1 = pd.Series(data1)
print(s1)

#----------------------------------------------------------------------------------------------------------------------------
# Series 인덱싱 및 슬라이싱 : 정수형, 문자열 등 다양한 인덱스 사용 가능 / 슬라이싱을 통한 부분 데이터 선택 가능
import pandas as pd

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 시리즈 인덱싱
print(s['a'])  # 10
print(s[['a', 'c', 'e']])  # a    10, c    30, e    50
print(s[:3])  # a    10, b    20, c    30
print(s[s > 30])  # d    40, e    50

#----------------------------------------------------------------------------------------------------------------------------
# 인덱스와 값을 포함한 Pandas Series 데이터를 사용하여 그래프를 그리는 예제
import pandas as pd
import matplotlib.pyplot as plt

# 시리즈 데이터 생성
sales = pd.Series([100, 120, 150, 160, 180], index=['Jan', 'Feb', 'Mar', 'Apr', 'May'])

# 막대 그래프 그리기
plt.bar(sales.index, sales.values)

# 축과 제목 설정
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')

# 그래프 표시
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 기본 산술 연산
import pandas as pd

# 시리즈 생성
data1 = {'a': 1, 'b': 2, 'c': 3}
data2 = {'a': 10, 'c': 30, 'd': 40}
s1 = pd.Series(data1)
s2 = pd.Series(data2)

# 덧셈 연산
s = s1 + s2
print(s)  # a    11.0, b     NaN, c    33.0, d     NaN
          # dtype: float64

#----------------------------------------------------------------------------------------------------------------------------
# 뺄셈 연산
s = s1 - s2
print(s)  # a    -9.0, b     NaN, c   -27.0, d     NaN
          # dtype: float64

#----------------------------------------------------------------------------------------------------------------------------
# 곱셈 연산
s = s1 * s2
print(s)  # a    10.0, b     NaN, c    90.0, d     NaN
          # dtype: float64

#----------------------------------------------------------------------------------------------------------------------------
# 나눗셈 연산
s = s1 / s2
print(s)  # a    0.1 , b     NaN, c    0.1 , d     NaN
          # dtype: float64


#----------------------------------------------------------------------------------------------------------------------------
# 집계 함수 사용 
import pandas as pd

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 집계 함수 예시
print(s.sum())  # 150
print(s.mean())  # 30.0
print(s.std())  # 15.811388300841896
print(s.max())  # 50
print(s.min())  # 10

#=============================================================================================================================
# DataFrame : 2차원 테이블 형태의 자료구조 / 인덱스와 열(column)로 구성된 데이터
import pandas as pd
import numpy as np

# 데이터프레임 생성 방법 1: 딕셔너리를 이용한 데이터프레임 생성
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df1)

#----------------------------------------------------------------------------------------------------------------------------
# 데이터프레임 생성 방법 2: 리스트를 이용한 데이터프레임 생성
data = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
df2 = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df2)

#----------------------------------------------------------------------------------------------------------------------------
# 데이터프레임 생성 방법 3: Numpy 배열을 이용한 데이터프레임 생성
arr = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df3)

#----------------------------------------------------------------------------------------------------------------------------
# 데이터프레임 생성 방법 4: 시리즈를 이용한 데이터프레임 생성
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
s3 = pd.Series([7, 8, 9])
df4 = pd.DataFrame({'A': s1, 'B': s2, 'C': s3})
print(df4)

#----------------------------------------------------------------------------------------------------------------------------
# 데이터프레임 생성 방법 5: 외부 데이터 파일을 이용한 데이터프레임 생성
df5 = pd.read_csv('data.csv')
print(df5)

#----------------------------------------------------------------------------------------------------------------------------
# 데이터프레임 데이터를 사용하여 그래프를 그리는 예제
import pandas as pd
import matplotlib.pyplot as plt

# 데이터프레임 생성
data = {
    'year': [2010, 2011, 2012, 2013, 2014],
    'sales': [100, 120, 150, 160, 180],
    'expenses': [80, 90, 100, 110, 120]
}

df = pd.DataFrame(data)

# 선 그래프 그리기
plt.plot(df['year'], df[['sales', 'expenses']])

# 축과 제목 설정
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Sales vs Expenses')

# 범례 추가
plt.legend(['Sales', 'Expenses'])

# 그래프 표시
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# DataFrame 정보 확인 예제
# 데이터프레임 정보 확인
    # head(): 데이터프레임에서 상위 5개 데이터를 출력합니다.
    # tail(): 데이터프레임에서 하위 5개 데이터를 출력합니다.
    # info(): 데이터프레임의 정보를 출력합니다. 열 이름, 데이터 타입, 결측치 개수 등을 확인할 수 있습니다.
    # describe(): 데이터프레임에서 수치형 열의 기술 통계 정보를 출력합니다.
    # columns: 데이터프레임의 열 이름을 출력합니다.
    # index: 데이터프레임의 행 인덱스를 출력합니다.
    # dtypes: 데이터프레임의 열의 데이터 타입을 출력합니다.
    # shape: 데이터프레임의 크기를 출력합니다.
    # isnull().sum(): 데이터프레임에서 결측치의 개수를 출력합니다.
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 데이터프레임 정보 출력
print(df.head())            # 상위 5개 데이터 출력
print(df.tail())            # 하위 5개 데이터 출력
print(df.info())            # 데이터프레임 정보 출력
print(df.describe())        # 수치형 열의 기술 통계 정보 출력
print(df.columns)           # 열 이름 출력
print(df.index)             # 행 인덱스 출력
print(df.dtypes)            # 열의 데이터 타입 출력
print(df.shape)             # 데이터프레임의 크기 출력
print(df.isnull().sum())    # 결측치 개수 출력

#----------------------------------------------------------------------------------------------------------------------------
# DataFrame 인덱싱 및 슬라이싱
# 열(column) 선택 방법
    # df['열인덱스']
    # df.열인덱스
    # df.loc[조건, 열]
    # df.iloc[ ]

import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)

#----------------------------------------------------------------------------------------------------------------------------
# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)

#----------------------------------------------------------------------------------------------------------------------------
# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

#----------------------------------------------------------------------------------------------------------------------------
# 열 선택 방법 4: loc[]를 이용한 열 선택
name_col = df.loc[:, 'name'] #df.loc[ ] : 열인덱스(열이름)를 사용
print(name_col)

#----------------------------------------------------------------------------------------------------------------------------
# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1]] # df.iloc[ ] : 위치 인덱스 사용
print(name_age_col)


#----------------------------------------------------------------------------------------------------------------------------
# 열 선택을 사용한 그래프 예제
import pandas as pd
import matplotlib.pyplot as plt

# 데이터프레임 생성
data = {
    'year': [2017, 2018, 2019, 2020, 2021],
    'A_product_sales': [6, 7, 8, 9, 10],
    'B_product_sales': [11, 12, 13, 14, 15]
}

df = pd.DataFrame(data)

# 특정 열 선택하여 연산 수행 후 결과를 새로운 열로 추가
df['total'] = df['A_product_sales'] + df['B_product_sales']

# 새로 추가한 열을 이용해서 그래프 그리기
plt.bar(df['year'], df['total'])  

plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Sales per Year')

plt.show()


#----------------------------------------------------------------------------------------------------------------------------
# 행(row) 선택 방법 : 인덱싱 (.loc 또는 .iloc 사용):
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 단일 행 선택: df.loc[row_label] 또는 df.iloc[row_index]
row1 = df.loc[2]  # 행인덱스를 사용하여 선택
row2 = df.iloc[3]  # 위치 인덱스를 사용하여 선택

print("단일 행 선택:")
print(row1)
print(row2)

#----------------------------------------------------------------------------------------------------------------------------
# 여러 행 선택: df.loc[start_label:end_label] 또는 df.iloc[start_index:end_index]
rows1 = df.loc[1:3]  # 행인덱스 범위를 사용하여 선택
rows2 = df.iloc[2:4]  # 위치인덱스 범위를 사용하여 선택

print("\n여러 행 선택:")
print(rows1)
print(rows2)

#----------------------------------------------------------------------------------------------------------------------------
# 특정 조건에 맞는 행 선택: df.loc[condition]
selected_rows = df.loc[df['age'] > 30]

print("\n조건에 맞는 행 선택:")
print(selected_rows)

#----------------------------------------------------------------------------------------------------------------------------
# 불리언 인덱싱 (특정 조건에 맞는 행 선택): df[condition]
selected_rows = df[(df['age'] > 30) & (df['city'] == 'London')]

print(selected_rows)

#----------------------------------------------------------------------------------------------------------------------------
# query() 메서드를 사용한 조건식을 이용한 행 선택: df.query(condition)
selected_rows = df.query("age > 30 and city == 'London'")

print(selected_rows)

#----------------------------------------------------------------------------------------------------------------------------
# isin() 메서드를 사용하여 여러 값에 해당하는 행 선택: df[df['column'].isin([value1, value2, ...])]
selected_rows = df[df['name'].isin(['Alice', 'Charlie', 'Eva'])]

print(selected_rows)

#----------------------------------------------------------------------------------------------------------------------------
# 특정 행과 열을 동시에 선택하는 방법 : df.loc를 사용하여 조건과 열을 함께 지정하는 것
# df.loc[조건, 열]
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [25, 30, 35, 40, 45],
    'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']
}

df = pd.DataFrame(data)

# 조건과 열을 동시에 사용하여 행 및 열 선택
selected_rows_columns = df.loc[(df['age'] > 30) & (df['city'] == 'London'), ['name', 'age']]
print(selected_rows_columns)

#----------------------------------------------------------------------------------------------------------------------------
# 열선택과 행선택을 동시에 사용해서 그래프를 그리는 예제
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'year': [2017, 2018, 2019, 2020, 2021],
    'A_product_sales': [6, 7, 8, 9, 10],
    'B_product_sales': [11, 12, 13, 14, 15],
    'C_product_sales': [9, 8, 7, 6, 5]
}

df = pd.DataFrame(data)

df = df.loc[df['year'] >=2019, ['year', 'A_product_sales', 'B_product_sales']]
                                
plt.plot(df['year'], df['A_product_sales'], marker = 'o', label = 'A_Product')
plt.plot(df['year'], df['B_product_sales'], marker = 'o', label = 'B_Product')

plt.legend()
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# DataFrame 연산 : 기본 산술 연산 가능 / 집계 함수 사용 가능 / 열 및 행을 기준으로 연산 가능
import pandas as pd

data1 = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
data2 = {'A': [9, 8, 7], 'B': [6, 5, 4], 'C': [3, 2, 1]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 기본 연산
print(df1 + df2)

#----------------------------------------------------------------------------------------------------------------------------
# 집계 함수
print(df1.mean())  #열 기준 
print(df1.mean(axis=1))  #행 기준

#----------------------------------------------------------------------------------------------------------------------------
import pandas as pd

data = {'A': [1, 2, 3, 4, 5, 3]}
df = pd.DataFrame(data)

#----------------------------------------------------------------------------------------------------------------------------
# 평균 (Mean)
mean_value = df['A'].mean()
print(f"Mean: {mean_value}")  # 결과: 3.0

#----------------------------------------------------------------------------------------------------------------------------
# 중앙값 (Median)
median_value = df['A'].median()
print(f"Median: {median_value}")  # 결과: 3.0

#----------------------------------------------------------------------------------------------------------------------------
# 최빈값 (Mode)
mode_value = df['A'].mode()
print(f"Mode: {mode_value[0]}")  # 결과: 3

#----------------------------------------------------------------------------------------------------------------------------
# 분산 (Variance)
variance_value = df['A'].var()
print(f"Variance: {variance_value}")  # 결과: 2.0

#----------------------------------------------------------------------------------------------------------------------------
# 표준편차 (Standard Deviation)
std_value = df['A'].std()
print(f"Standard Deviation: {std_value}")  # 결과: 1.4142135623730951


#=============================================================================================================================
# Pandas 데이터 입출력
# CSV 파일 읽기: pandas의 read_csv() 함수를 이용하여 CSV 파일을 불러올 수 있습니다.
import pandas as pd

df = pd.read_csv('data.csv')

#----------------------------------------------------------------------------------------------------------------------------
# Excel 파일 읽기: pandas의 read_excel() 함수를 이용하여 Excel 파일을 불러올 수 있습니다.
import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

#----------------------------------------------------------------------------------------------------------------------------
# CSV, Excel, SQL 등 다양한 형식으로 파일을 저장할 수 있음
import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# CSV 파일 쓰기
df.to_csv('output.csv', index=False)

# Excel 파일 쓰기
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)


#=============================================================================================================================
# 데이터 전처리
# 중복 데이터 처리
import pandas as pd

# 예제 데이터
data = {'A': [1, 2, 2], 'B': [4, 5, 5], 'C': [7, 8, 8]}
df = pd.DataFrame(data)

# (중복 확인) 찾기 : df.duplicated()
print(df.duplicated())
# 결과:
# 0    False
# 1    False
# 2     True

# (중복) 제거 : df.drop_duplicates()
deduplicated_df = df.drop_duplicates()
print(deduplicated_df)
# 결과:
#    A  B  C
# 0  1  4  7
# 1  2  5  8

#----------------------------------------------------------------------------------------------------------------------------
# 데이터 형 변환
# astype() :데이터의 자료형을 변환해주는 함수
# int 또는 int64: 정수형
# float 또는 float64: 실수형
# bool 또는 bool_: 불리언형
# str 또는 object: 문자열형
# category: 범주형
# datetime64: 날짜/시간형

import pandas as pd

# 데이터프레임 생성
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'str_col': ['1', '2', '3', '4', '5'],
        'bool_col': [True, False, True, False, True],
        'category_col': ['a', 'b', 'c', 'a', 'b'],
        'date_col': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']}

df = pd.DataFrame(data)

# 열 데이터 형 변환
df['int_col'] = df['int_col'].astype(float)  # 정수형 -> 실수형
df['float_col'] = df['float_col'].astype(int)  # 실수형 -> 정수형
df['str_col'] = df['str_col'].astype(bool)  # 문자열 -> 불리언형
df['bool_col'] = df['bool_col'].astype(str)  # 불리언형 -> 문자열형
df['category_col'] = df['category_col'].astype('category')  # 문자열 -> 범주형
df['date_col'] = pd.to_datetime(df['date_col'])  # 문자열 -> 날짜/시간형

# 데이터프레임 정보 출력
print(df.dtypes)

#----------------------------------------------------------------------------------------------------------------------------
# 데이터 형 변환 : to_numeric(): 데이터를 수치형으로 변환해주는 함수
import pandas as pd

# 데이터프레임 생성
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'str_col': ['1', '2', '3', '4', '5']}

df = pd.DataFrame(data)

# 열 데이터 형 변환
df['int_col'] = pd.to_numeric(df['int_col'])  # 정수형 -> 숫자형
df['float_col'] = pd.to_numeric(df['float_col'])  # 실수형 -> 숫자형
df['str_col'] = pd.to_numeric(df['str_col'])  # 문자열 -> 숫자형

# 데이터프레임 출력
print(df)

#----------------------------------------------------------------------------------------------------------------------------
# 데이터 형 변환 : apply():데이터프레임이나 시리즈에서 함수를 적용하여 새로운 결과를 반환하는 메소드
# df.apply(func, axis=0, **kwargs)
# func: 적용할 함수
# axis: 적용할 축. 0은 열, 1은 행입니다. 기본값은 0입니다.
# **kwargs: func 함수에 추가적으로 전달할 인수입니다.

import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': ['25', '30', '35'],
        'score1': [80, 70, 85],
        'score2': [85, 75, 90]}

df = pd.DataFrame(data)

# apply() 메소드를 이용하여 모든 문자열 값을 대문자로 변환
df['name'] = df['name'].apply(lambda x: x.upper())
df['age'] = df['age'].apply(int)

print(df)

#----------------------------------------------------------------------------------------------------------------------------
# 문자열 처리 : 문자열 데이터를 처리하기 위한 다양한 메소드 제공
# .str 액세서를 사용하여 문자열 함수를 적용
    # upper(): 모든 문자를 대문자로 변환합니다.
    # lower(): 모든 문자를 소문자로 변환합니다.
    # strip(): 양쪽 끝의 공백을 제거합니다.
    # lstrip(): 왼쪽 끝의 공백을 제거합니다.
    # rstrip(): 오른쪽 끝의 공백을 제거합니다.
    # split(): 주어진 구분자를 기준으로 문자열을 분할합니다.
    # contains(): 문자열에서 특정 문자열이 포함되어 있는지 확인합니다.
    # replace(): 문자열에서 특정 문자열을 다른 문자열로 대체합니다.
    # slice(): 문자열에서 일부 문자를 추출합니다.
    # len(): 문자열의 길이를 반환합니다.
    # startswith(): 문자열이 특정 문자열로 시작하는지 확인합니다.
    # endswith(): 문자열이 특정 문자열로 끝나는지 확인합니다.
import pandas as pd

# 샘플 데이터 생성
data = {
    'text': ['Hello, World!', 'Pandas is great', 'Python is awesome']
}
df = pd.DataFrame(data)

# 문자열 처리 작업
df['lower'] = df['text'].str.lower()  # 모든 문자를 소문자로 변환
df['words'] = df['text'].str.split()  # 공백을 기준으로 단어 분할
df['no_punctuation'] = df['text'].str.replace('[^\w\s]', '', regex=True) # 구두점, 기호 제거 # [^\w\s] 패턴은 단어 문자와 공백 문자가 아닌 모든 문자
df['word_count'] = df['text'].str.split().str.len()  # 단어 개수 계산

print(df.iloc[:, 1:]) #1번 열부터 마지막 열까지

#----------------------------------------------------------------------------------------------------------------------------
#열 추가
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 추가 방법 1: 기존 열을 이용하여 새로운 열 추가
df['age2'] = df['age'] + 1

# 열 추가 방법 2: insert() 메소드를 이용하여 특정 위치에 열 추가
df.insert(loc=2, column='gender', value=['F', 'M', 'M', 'M', 'F'])

# 열 추가 방법 3: assign() 메소드를 이용하여 여러 개의 열 한 번에 추가
df = df.assign(age3=[26, 31, 36, 41, 46], height=[160, 170, 180, 175, 165])

# 출력
print(df)

#----------------------------------------------------------------------------------------------------------------------------
#행 추가
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 추가 방법 1: append() 메소드를 이용하여 단일 행 추가
new_row = {'name': 'Frank', 'age': 50, 'city': 'Seoul'}
df = df.append(new_row, ignore_index=True)

# 행 추가 방법 2: append() 메소드를 이용하여 여러 행 추가
new_rows = [{'name': 'George', 'age': 22, 'city': 'Toronto'},
            {'name': 'Helen', 'age': 27, 'city': 'Sydney'}]
df = df.append(new_rows, ignore_index=True)

# 출력
print(df)

#----------------------------------------------------------------------------------------------------------------------------
# 삭제
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 삭제 방법 1: drop() 메소드를 이용하여 단일 행 삭제
df = df.drop(0)

# 행 삭제 방법 2: drop() 메소드를 이용하여 여러 행 삭제
df = df.drop([1, 2])

# 열 삭제 방법 1: drop() 메소드를 이용하여 단일 열 삭제
df = df.drop('age', axis=1)

# 열 삭제 방법 2: drop() 메소드를 이용하여 여러 열 삭제
df = df.drop(['name', 'city'], axis=1)

# 출력
print(df)

#----------------------------------------------------------------------------------------------------------------------------
#재정렬
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 재정렬 방법 1: loc[]을 이용하여 행 순서 변경
df = df.loc[[4, 3, 2, 1, 0]]

# 행 재정렬 방법 2: sort_values() 메소드를 이용하여 열 기준으로 정렬
df = df.sort_values('age', ascending=False)

# 열 재정렬 방법 1: 열 이름 순서 변경
df = df[['city', 'name', 'age']]

# 열 재정렬 방법 2: 열 이름을 알파벳 순서로 정렬
df = df.reindex(sorted(df.columns), axis=1)

# 출력
print(df)

#----------------------------------------------------------------------------------------------------------------------------
#Concat : 데이터프레임을 수직(위-아래) 또는 수평(좌-우)으로 연결하는 데 사용
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']})

result = pd.concat([df1, df2], axis=0, ignore_index=True)

print(result)

#----------------------------------------------------------------------------------------------------------------------------
# Merge : 두 데이터프레임을 공통 열 또는 인덱스를 기준으로 병합하는 데 사용 <기본 조인 방법은 inner join>
import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                     'A': ['A0', 'A1', 'A3'],
                     'B': ['B0', 'B1', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                      'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']})

result = pd.merge(left, right, on='key')


print(result)

#----------------------------------------------------------------------------------------------------------------------------
# Join : 인덱스를 기준으로 두 데이터프레임을 병합하는 데 사용. <기본적으로 left join을 수행( how=＇inner'|'outer'|'right')> 
import pandas as pd

# 첫 번째 데이터프레임 생성
data1 = {'이름': ['John', 'Steve', 'Sarah'],
         '나이': [25, 32, 28],
         '성별': ['남', '남', '여']}
df1 = pd.DataFrame(data1)

# 두 번째 데이터프레임 생성
data2 = {'이름': ['Steve', 'Sarah', 'Mike'],
         '키': [180, 163, 190],
         '학년': ['2학년', '2학년', '3학년']}
df2 = pd.DataFrame(data2)

# 조인 작업 수행
# how='inner': 내부 조인
inner_join = df1.join(df2.set_index('이름'), on='이름', how='inner')
print("Inner Join:")
print(inner_join)


#----------------------------------------------------------------------------------------------------------------------------
# groupby() 함수 : 데이터프레임을 해당 열의 값에 따라 그룹화. 반환값은 그룹화된 데이터프레임을 나타내는 GroupBy 객체
# grouped = df.groupby('열 이름')
# grouped['열이름'].집계함수()

# count(): 그룹별로 데이터의 개수를 계산합니다.
# size(): 그룹별로 데이터의 크기를 계산합니다. count()와 다르게 NaN값도 포함합니다.
# sum(): 그룹별로 데이터의 합을 계산합니다.
# mean(): 그룹별로 데이터의 평균을 계산합니다.
# median(): 그룹별로 데이터의 중앙값을 계산합니다.
# min(): 그룹별로 데이터의 최솟값을 계산합니다.
# max(): 그룹별로 데이터의 최댓값을 계산합니다.
# std(): 그룹별로 데이터의 표준편차를 계산합니다.
# var(): 그룹별로 데이터의 분산을 계산합니다.
# sem(): 그룹별로 데이터의 표준오차를 계산합니다.
# describe(): 그룹별로 기술통계값을 계산합니다.
import pandas as pd


Data= {'name': ['Alice', 'Bob', 'Charlie', 'David','Emily', 'Frank'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 30, 35, 40, 45, 50],
        'score1': [80, 70, 85, 75, 90, 95],
        'score2': [85, 75, 90, 80, 95, 100]}

df = pd.DataFrame(data)

# count
print(df.groupby('gender')[['score1', 'score2']].count())

# size
print(df.groupby('gender')[['score1', 'score2']].size())

# sum
print(df.groupby('gender')[['score1', 'score2']].sum())

# mean
print(df.groupby('gender')[['score1', 'score2']].mean())

# median
print(df.groupby('gender')[['score1', 'score2']].median())

# min
print(df.groupby('gender')[['score1', 'score2']].min())

# max
print(df.groupby('gender')[['score1', 'score2']].max())

# '열 이름'은 그룹화된 데이터프레임에서 연산을 수행할 열의 이름
# '통계 함수'에는 원하는 통계 함수(예: mean, sum, count, min, max 등)
# result = grouped['열 이름'].agg(['통계 함수'])


#----------------------------------------------------------------------------------------------------------------------------
# agg 함수 : 다중 열에 대한 집계 함수를 적용하는 방법
# grouped = df.groupby(['열이름A’, ‘열이름B’])
# grouped.agg({'열1': '집계함수1', '열2': '집계함수2', ...})
import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': [1, 2, 3, 4, 5, 6, 7, 8],
    'D': [10, 20, 30, 40, 50, 60, 70, 80]
})
# A와 B 컬럼에 대해서 그룹화한 결과에 대해 C 컬럼에 대해서는 count 함수를 적용하고, D 컬럼에 대해서는 sum과 mean 함수를 각각 적용

result = df.groupby(['A', 'B']).agg({'C': 'count', 'D': ['sum', 'mean']})
print(result)

#----------------------------------------------------------------------------------------------------------------------------
import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
})

def my_func(x):
    return '-'.join(sorted(x))

result = df.groupby('A').agg({'B': my_func})

print(result)

#----------------------------------------------------------------------------------------------------------------------------
# Pivot_table : 데이터프레임에서 특정 열을 그룹화하여 행과 열을 피벗테이블 형태로 나타낼 수 있습니다.
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob'],
    'Date': ['Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2'],
    'Value': [10, 20, 15, 25, 30, 40, 35, 45]
})

result = df.pivot_table(index='Name', columns='Date', values='Value', aggfunc='mean')

print(result)

#----------------------------------------------------------------------------------------------------------------------------
import pandas as pd

# 매출 데이터 생성
data = {'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'], 
        'Time': ['Morning', 'Afternoon', 'Morning', 'Afternoon', 'Morning', 'Afternoon', 'Morning', 'Afternoon'],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
df = pd.DataFrame(data)

# 피벗테이블 생성
result = df.pivot_table(index='Region', columns='Time', values='Sales', aggfunc='sum')

print(result)

#----------------------------------------------------------------------------------------------------------------------------
import pandas as pd

# 고객 데이터 생성
data = {'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'], 
        'Age': [20, 30, 40, 50, 30, 40, 50, 60],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
df = pd.DataFrame(data)

# 피벗테이블 생성
result = df.pivot_table(index='Region', columns=pd.cut(df['Age'], [10, 30, 50, 70]), values='Sales', aggfunc='mean')

print(result)

#----------------------------------------------------------------------------------------------------------------------------
# cut 함수 : 주어진 데이터를 일정한 구간으로 나누어 범주형 데이터로 변환하는 함수. 생성된 카테고리는 groupby나 pivot_table과 같은 함수에서 인덱스 또는 열로 사용 가능.
import pandas as pd

# 나이 데이터 생성
ages = pd.DataFrame({'age': [22, 44, 65, 86, 27, 19, 51, 92, 33, 35, 38, 42, 14, 50, 78]})

# 연령대 구간 지정
bins = [0, 20, 40, 60, 80, 100]

# 연령대 카테고리 생성
age_categories = pd.cut(ages['age'], bins)

# 데이터프레임에 새로운 카테고리 열 추가
ages['age_categories'] = age_categories

# 결과 확인
print(ages)
result = pd.pivot_table(ages, index='age_categories', aggfunc='count')
print(result)

#----------------------------------------------------------------------------------------------------------------------------
# 시계열 데이터 변환 : 문자열이나 다른 형식의 날짜와 시간 데이터를 datetime 형식으로 변환할 때 사용 <pd.to_datetime()>
import pandas as pd

data = {'date': ['2021-08-15', '2021-08-16', '2021-08-17'],
        'value': [100, 200, 150]}
df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])
print(df)

#----------------------------------------------------------------------------------------------------------------------------
# 문자열이 다른 형식으로 되어있을 경우 format 인자를 사용하여 문자열의 형식을 지정
import pandas as pd

# 날짜 데이터 생성
df = pd.DataFrame({'date': ['2022년 01월 01일', '2022년 01월 02일', '2022년 01월 03일']})

# 날짜 데이터를 datetime 형식으로 변환
df['date'] = pd.to_datetime(df['date'], format='%Y년 %m월 %d일')

# 년, 월, 일 컬럼 추출
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print(df)


#----------------------------------------------------------------------------------------------------------------------------
# pd.resample() : 기존의 데이터셋을 새로운 시간 간격에 맞추어 변환해줍니다.
import pandas as pd

data = {'date': ['2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02'],
        'location': ['서울', '서울', '부산', '부산', '대구', '대구'],
        'PM10': [50, 40, 45, 55, 60, 65],
        'PM2.5': [25, 20, 22, 28, 30, 35]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

df_monthly = df.groupby('location').resample('D', on='date').mean(numeric_only=True)
print(df_monthly)

# 시계열 데이터 변환
        # pd.resample()
        # 시간 간격(alias) 문자열
        # B: 평일(Business day) 기준으로 간격 지정
        # C: 사용자 지정 시간대 내에서의 주기마다 간격 지정
        # D: 달력 일(Day) 기준으로 간격 지정
        # W: 주(Week) 기준으로 간격 지정
        # M: 달(Month)의 마지막 날 기준으로 간격 지정
        # SM: 반월(Semi-Month) 기준으로 간격 지정 (월의 15일과 말일을 기준)
        # BM: 평일 기준으로 한 달의 마지막 날까지 간격 지정
        # CBM: 사용자 지정 시간대 내에서 평일 기준으로 한 달의 마지막 날까지 간격 지정
        # MS: 달(Month)의 시작일 기준으로 간격 지정
        # SMS: 반월(Semi-Month) 기준으로 간격 지정 (월의 1일과 15일을 기준)
        # BMS: 평일 기준으로 한 달의 시작일부터 마지막 날까지 간격 지정
        # CBMS: 사용자 지정 시간대 내에서 평일 기준으로 한 달의 시작일부터 마지막 날까지 간격 지정
        # Q: 분기(Quarter)의 마지막 날 기준으로 간격 지정
        # BQ: 평일 기준으로 분기의 마지막 날까지 간격 지정
        # QS: 분기(Quarter)의 시작일 기준으로 간격 지정
        # BQS: 평일 기준으로 분기의 시작일부터 마지막 날까지 간격 지정
        # A: 해(Year)의 마지막 날 기준으로 간격 지정
        # BA: 평일 기준으로 해의 마지막 날까지 간격 지정
        # AS: 해(Year)의 시작일 기준으로 간격 지정
        # BAS: 평일 기준으로 해의 시작일부터 마지막 날까지 간격 지정


# to_datetime에서 자동으로 인식하는 날짜 형식
        # %Y-%m-%d %H:%M:%S.%f
        # %Y-%m-%d %H:%M:%S
        # %Y-%m-%d %H:%M
        # %Y-%m-%d
        # %m/%d/%Y %H:%M:%S
        # %m/%d/%Y %H:%M
        # %m/%d/%Y
        # %m/%d/%y %H:%M:%S
        # %m/%d/%y %H:%M
        # %m/%d/%y

