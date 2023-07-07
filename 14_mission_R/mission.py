from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import seaborn as sn

## 1. 데이터 불러오기 및 확인하기
iris = load_iris()
# print('타킷 : ', iris['target']) # 0 : setosa / 1 : versicolor / 2 : virginica -> 종

# iris 데이터의 전반적인 정보 확인
df = pd.DataFrame(iris.data, columns=iris['feature_names'])
df.columns = ['꽃받침 길이', '꽃받침 너비', '꽃잎 길이', '꽃잎 너비'] # column 이름 재정의
df['품종 번호'] = iris['target'] # 품종 번호 col 추가
df.info()


## 2. 전처리
# 결측치 확인 및 처리
df.isnull().sum() # 결측치 존재 X

# 중복값 확인 및 처리
df.duplicated().sum() # 1개의 중복값 존재
df.loc[df.duplicated(), :] # 142번 데이터가 중복임을 확인.
df.loc[(df['꽃받침 길이'] == 5.8)&(df['꽃받침 너비'] == 2.7)&(df['꽃잎 길이'] == 5.1)&(df['꽃잎 너비'] == 1.9)] # 142번과 동일한 데이터 가진 데이터 찾기(101)


# 통계 정보 확인
#df.describe()

# EDA(Exploratory Data Analysis)
# 평균 구하기
