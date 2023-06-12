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

