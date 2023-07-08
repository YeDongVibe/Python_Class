from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# 한글 폰트 설정
rc('font', family='Malgun Gothic')

# 1. 데이터 불러오기 및 확인하기
iris = load_iris()

# iris 데이터의 전반적인 정보 확인
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.columns = ['꽃받침_길이', '꽃받침_너비', '꽃잎_길이', '꽃잎_너비']  # column 이름 재정의
df['품종_번호'] = iris.target  # 품종 번호 col 추가
df['품종_번호'] = df['품종_번호'].astype('category')  # '품종_번호' 열을 카테고리 데이터로 변환

# 결측치 확인 및 처리
df.isnull().sum()  # 결측치 존재 X

# 중복값 확인 및 처리
df.duplicated().sum()  # 1개의 중복값 존재
df.loc[df.duplicated(), :]  # 142번 데이터가 중복임을 확인.

df['품종_번호'].value_counts()  # 각 50개씩 존재

# 상관 관계 분석
df.corr()

# 통계 정보 확인
df.describe()

# 이상치 확인을 위한 boxplot
plt.figure(figsize=(10, 8))
axes = plt.subplots(2, 2)[1]
sn.boxplot(data=df, x='품종_번호', y='꽃받침_길이', ax=axes[0, 0])
sn.boxplot(data=df, x='품종_번호', y='꽃받침_너비', ax=axes[0, 1])
sn.boxplot(data=df, x='품종_번호', y='꽃잎_길이', ax=axes[1, 0])
sn.boxplot(data=df, x='품종_번호', y='꽃잎_너비', ax=axes[1, 1])
plt.tight_layout()
plt.show()

# 전체적으로 확인
sn.pairplot(df, hue="품종_번호")

# 꽃잎길이와 꽃잎너비
sn.pairplot(data=df, vars=["꽃잎_너비", "꽃잎_길이"], hue="품종_번호", height=4)

print('k-최근접 이웃')
# k-최근접 이웃 이용
# 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(df, df['품종_번호'], random_state=0)

# 데이터 확인 위해 추가한 col 삭제
X_train = X_train.drop('품종_번호', axis=1)
X_test = X_test.drop('품종_번호', axis=1)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape:", X_new.shape)

prediction = knn.predict(X_new)
print("예측:", prediction)
print("예측한 타깃의 이름:", iris.target_names[prediction])

y_pred = knn.predict(X_test)
print(X_test[:5])
print("테스트 세트에 대한 예측값:\n", y_pred)

accuracy = np.mean(y_pred == y_test)
print("테스트 세트의 정확도: {:.5f}".format(accuracy))

classification_report_str = classification_report(y_test, y_pred)
print("분류 보고서:\n", classification_report_str)

print('랜덤포레스트')
# 랜덤포레스트 이용
X_train, X_test, y_train, y_test = train_test_split(df, df['품종_번호'], test_size=0.2, stratify=df['품종_번호'], random_state=0)  # random 시드값

# 데이터 확인 위해 추가한 col삭제
X_train = X_train.drop('품종_번호', axis=1)
X_test = X_test.drop('품종_번호', axis=1)

random_forest = RandomForestClassifier(random_state=32)
random_forest.fit(X_train, y_train)
y_pred = random_forest.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

print()
print(classification_report(y_test, y_pred))
