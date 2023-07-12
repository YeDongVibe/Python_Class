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
from sklearn.decomposition import PCA



rc('font', family='Malgun Gothic')

## 1. 데이터 불러오기 및 확인하기
iris = load_iris()

# iris 데이터의 전반적인 정보 확인
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.columns = ['꽃받침_길이', '꽃받침_너비', '꽃잎_길이', '꽃잎_너비'] # column 이름 재정의
df['품종_번호'] = iris.target # 품종 번호 col 추가
df['품종_번호'] = df['품종_번호'].astype('category') # '품종_번호' 열을 카테고리 데이터로 변환
df.info()
df.describe()


# 결측치 확인 및 처리
df.isnull().sum() # 결측치 존재 X

# 중복값 확인 및 처리
df.duplicated().sum() # 1개의 중복값 존재
df.loc[df.duplicated(), :] # 142번 데이터가 중복임을 확인.
df.loc[(df['꽃받침_길이'] == 5.8) & (df['꽃받침_너비'] == 2.7) & (df['꽃잎_길이'] == 5.1) & (df['꽃잎_너비'] == 1.9)] # 142번과 동일한 데이터 가진 데이터 찾기(101)
# 1개의 중복값이 존재하나 영향을 끼치지 않을 것 이기에 제거는 하지 않음.

df['품종_번호'].value_counts() # 각 50개씩 존재

# 상관 관계 분석
df.corr()

# 통계 정보 확인
df.describe()

# 이상치 확인을 위한 boxplot
plt.figure(figsize=(10, 8))
axes = plt.subplots(2,2)[1]
sn.boxplot(data=df, x='품종_번호', y='꽃받침_길이', ax=axes[0,0])
sn.boxplot(data=df, x='품종_번호', y='꽃받침_너비', ax=axes[0,1])
sn.boxplot(data=df, x='품종_번호', y='꽃잎_길이', ax=axes[1,0])
sn.boxplot(data=df, x='품종_번호', y='꽃잎_너비', ax=axes[1,1])
plt.tight_layout()
plt.show()
# 크게 벗어나는 구간이 없으므로 별도 처리는 하지 않을예정.

# 전체적으로 확인
sn.pairplot(df, hue="품종_번호")
# 꽃잎길이와 꽃잎너비
sn.pairplot(data=df, vars=["꽃잎_너비", "꽃잎_길이"], hue="품종_번호", height=4)


# 데이터 나누기 및 확인
X_train, X_test, y_train, y_test = train_test_split(
    df, df['품종_번호'], random_state=0)

print("X_train 크기:", X_train.shape)
print("y_train 크기:", y_train.shape)
print("X_test 크기:", X_test.shape)
print("y_test 크기:", y_test.shape)

# 데이터 확인 위해 추가한 col 삭제
X_train = X_train.drop('품종_번호', axis=1)
X_test = X_test.drop('품종_번호', axis=1)

iris_dataframe = pd.DataFrame(X_train, columns=iris.feature_names)

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

# 시각화
# 주성분 분석을 위한 객체 생성
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)

knn.fit(X_train_pca, y_train)

# 결정 경계 시각화를 위한 그리드 생성
h = 0.02  # mesh의 스텝 사이즈
x_min, x_max = X_train_pca[:, 0].min() - 1, X_train_pca[:, 0].max() + 1
y_min, y_max = X_train_pca[:, 1].min() - 1, X_train_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# 결정 경계 예측
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 결정 경계 시각화
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.RdYlBu) # 가시성을 위해 contourf 사용
scatter = plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, cmap=plt.cm.Set1)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('KNN Decision Boundary')
# 범례(legend) 설정
handles, labels = scatter.legend_elements()
plt.legend(handles, iris.target_names)
plt.show()


X_train, X_test, y_train, y_test = train_test_split(df, df['품종_번호'], test_size=0.2, stratify=df['품종_번호'], random_state=0) # random 시드값

# 데이터 확인 위해 추가한 col삭제
X_train = X_train.drop('품종_번호', axis=1)
X_test = X_test.drop('품종_번호', axis=1)

#랜덤 포레스트 모델 학습
random_forest = RandomForestClassifier(random_state=32)
random_forest.fit(X_train, y_train)
y_pred = random_forest.predict(X_test)

#정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
print()
print(classification_report(y_test, y_pred))

#시각화

# 트리의 중요도 계산
importance = random_forest.feature_importances_

# 중요도 시각화
plt.figure(figsize=(10, 6))
plt.bar(df.columns[:-1], importance)
plt.xlabel('특성')
plt.ylabel('중요도')
plt.title('Random Forest Feature Importance')
plt.xticks(rotation=45)
plt.show()

# 트리의 결정 경계 시각화를 위해 2개의 특성만 선택 (꽃받침_길이, 꽃잎_길이)
X_train_selected = X_train[['꽃잎_길이', '꽃잎_너비']]
X_test_selected = X_test[['꽃잎_길이', '꽃잎_너비']]

random_forest_selected = RandomForestClassifier(random_state=32)
random_forest_selected.fit(X_train_selected, y_train)

# 결정 경계 시각화를 위해 데이터의 최솟값과 최댓값 사이를 나누는 그리드 생성
x_min, x_max = X_train_selected['꽃잎_길이'].min() - 1, X_train_selected['꽃잎_길이'].max() + 1
y_min, y_max = X_train_selected['꽃잎_너비'].min() - 1, X_train_selected['꽃잎_너비'].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# 결정 경계 예측
Z = random_forest_selected.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 결정 경계 시각화
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.RdYlBu)
plt.scatter(X_train_selected['꽃잎_길이'], X_train_selected['꽃잎_너비'], c=y_train, edgecolors='k', cmap=plt.cm.Set1)
plt.xlabel('꽃잎_길이')
plt.ylabel('꽃잎_너비')
plt.title('Random Forest Decision Boundary')
plt.show()


