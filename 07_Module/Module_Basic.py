#모듈 불러오기
#import <module-name>

#dir() 함수 : 모듈이나 클래스에 포함된 변수, 메소드, 클래스 등의 속성들을 확인할 수 있습니다.
import random

print('='*70)
print(dir(random)) # random 모듈 내에 포함된 변수, 함수, 클래스 등을 나열합니다.
print('-'*70)
print(help(random.choice)) # random 모듈 내에 포함된 choice 함수의 도움말을 출력합니다.
print('-'*70)

#from import : from import는 모듈에서 특정 변수, 함수, 클래스 등을 가져올 때 사용됩니다
from math import sqrt, pi

print('='*70)
print(sqrt(4))  # 출력 결과: 2.0 # from ~~ import ~~ 이렇게 쓰면 함수이름을 그대로 가져와 사용 가능
print('-'*70)
print(pi)  # 출력 결과: 3.141592653589793
print('-'*70)

#from import * : *를 사용하여 모든 변수, 함수, 클래스 등을 가져오는 것은 권장되지 않습니다. 왜냐하면, 모듈에서 모든 것을 가져오면 현재 스코프에서 이름 충돌이 일어날 수 있기 때문입니다. 또한, 모듈에서 사용하지 않는 함수나 클래스도 불필요하게 가져오기 때문에 메모리 낭비가 발생할 수 있습니다.
from math import *

print('='*70)
print(sqrt(9))  # 출력 결과: 3.0
print('-'*70)
print(pi)  # 출력 결과: 3.141592653589793
print('-'*70)
print(sin(pi/2))  # 출력 결과: 1.0
print('-'*70)

#import as : 모듈을 불러올 때 해당 모듈에 별칭(alias)을 지어주는 방법입니다.
import math as m

print('='*70)
print(m.sqrt(4))  # 2.0
print('-'*70)
print(m.pi)  # 3.141592653589793
print('-'*70)

#sys.path : 현재 파이썬 인터프리터가 모듈을 검색할 경로들을 담고 있는 리스트
import os, sys

print('='*70)
print(os.getcwd()) #현재 디렉토리 표시
print('-'*70)
print(sys.path) #환경변수에 지정된 디렉토리
print('-'*70)

#================================================================================================================
#사용자 정의 모듈
#my_module.py : Python 파일을 만들어서 제작(사용자 모듈 제작)
# def greet(name):
#     print(f"Hello, {name}!")

#main.py : 사용자가 만든 모듈을 import하여 사용
# import my_module

# my_module.greet("Alice")  # "Hello, Alice!" 출력

#-----------------------------------------------------------------------------------------------------------------
#if __name__ == '__main__' : 메인 파일에서는 사용 가능하지만 다른 모듈에서 import할 때는 사용 불가
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    print(add(3, 5))
    print(subtract(10, 7))

#================================================================================================================
#OS
import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print("현재 작업 디렉토리:", current_dir)

# 새로운 디렉토리 생성
new_dir = "new_directory"
os.mkdir(new_dir)
print(f"새로운 디렉토리 '{new_dir}'가 생성되었습니다.")

# 생성한 디렉토리 내에 파일 생성
new_file = "new_file.txt"
with open(os.path.join(new_dir, new_file), "w") as f:
    f.write("새로운 파일 내용")
print(f"'{new_file}' 파일이 '{new_dir}' 디렉토리 내에 생성되었습니다.")

# 지정된 디렉토리의 파일 및 디렉토리 목록 확인
list_dir = os.listdir(new_dir)
print(f"'{new_dir}' 디렉토리 내의 파일 및 디렉토리 목록: {list_dir}")

# 파일인지 디렉토리인지 확인
for item in list_dir:
    item_path = os.path.join(new_dir, item)
    if os.path.isfile(item_path):
        print(f"'{item_path}'는 파일입니다.")
    elif os.path.isdir(item_path):
        print(f"'{item_path}'는 디렉토리입니다.")

# 파일 삭제
os.remove(os.path.join(new_dir, new_file))
print(f"'{new_file}' 파일이 삭제되었습니다.")

# 디렉토리 삭제
os.rmdir(new_dir)
print(f"'{new_dir}' 디렉토리가 삭제되었습니다.")

#================================================================================================================
#SYS
import sys

# sys.argv 예시
print("명령행 인자(argument) 리스트:", sys.argv)

# sys.getsizeof() 예시
a = [1, 2, 3]
print("a의 크기:", sys.getsizeof(a))

# sys.stdin, sys.stdout, sys.stderr 예시
sys.stdout.write("표준 출력 테스트\n")
sys.stderr.write("표준 오류 출력 테스트\n")
input_data = sys.stdin.readline().strip()
print("입력값:", input_data)

# sys.version, sys.platform 예시
print("현재 파이썬 버전:", sys.version)
print("현재 시스템 플랫폼:", sys.platform)

# sys.path 예시
print("모듈 검색 경로:", sys.path)

#================================================================================================================
#Math
import math

# 반올림 함수
print(math.ceil(3.2))    # 결과: 4
print(math.ceil(-3.2))   # 결과: -3

print(math.floor(3.2))   # 결과: 3
print(math.floor(-3.2))  # 결과: -4

print(round(3.2))        # 결과: 3
print(round(-3.2))       # 결과: -3
print(round(3.5))        # 결과: 4
print(round(-3.5))       # 결과: -4

print(math.trunc(3.7))    # 결과: 3
print(math.trunc(-3.7))   # 결과: -3

# 절댓값 함수
print(abs(3.2))          # 결과: 3.2
print(abs(-3.2))         # 결과: 3.2

print(math.fabs(3.2))     # 결과: 3.2
print(math.fabs(-3.2))    # 결과: 3.2

#================================================================================================================
#datetime
import datetime

# 현재 시간 정보 가져오기
now = datetime.datetime.now()
print("현재 시간:", now)

# 시간 정보를 직접 지정해서 datetime 객체 생성하기
dt = datetime.datetime(2022, 3, 11, 13, 30, 0)
print("직접 지정한 datetime 객체:", dt)

# datetime 객체에서 날짜 정보 가져오기
date = dt.date()
print("date 객체:", date)
print("년:", date.year)
print("월:", date.month)
print("일:", date.day)

# datetime 객체에서 시간 정보 가져오기
time = dt.time()
print("time 객체:", time)
print("시:", time.hour)
print("분:", time.minute)
print("초:", time.second)

# 날짜 간의 차이 계산하기
date1 = datetime.date(2022, 3, 1)
date2 = datetime.date(2022, 3, 11)
delta = date2 - date1
print("날짜 차이:", delta)
print("일수 차이:", delta.days)

# timedelta를 이용한 시간 간의 차이 계산하기
td = datetime.timedelta(hours=3, minutes=30)
print("시간 차이:", td)
print("총 분:", td.total_seconds() / 60)

# 날짜/시간 포맷 지정하기
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print("포맷 지정된 날짜:", formatted_date)
print("포맷 지정된 시간:", formatted_time)
print("포맷 지정된 datetime:", formatted_datetime)


#-----------------------------------------------------------------------------------------------------------------
#현재 날짜에서 100일, 1000일 후의 날짜를 계산하기
import datetime

# 현재 날짜
today = datetime.date.today()

# 100일 후의 날짜
hundred_days_later = today + datetime.timedelta(days=100)

# 1000일 후의 날짜
thousand_days_later = today + datetime.timedelta(days=1000)

# 결과 출력
print("100일 후:", hundred_days_later)
print("1000일 후:", thousand_days_later)

#================================================================================================================
#calendar
import calendar

# 2023년 3월의 달력을 출력합니다.
print("2023년 3월의 달력:")
print(calendar.month(2023, 3))

# 2023년 3월 15일의 요일을 확인합니다. (월요일: 0, 화요일: 1, ..., 일요일: 6)
year = 2023
month = 3
day = 15
weekday = calendar.weekday(year, month, day)
print("2023년 3월 15일은 요일 인덱스 {}에 해당하는 요일입니다.".format(weekday))

# 요일 인덱스를 사용하여 요일 이름을 가져옵니다.
weekday_name = calendar.day_name[weekday]
print("2023년 3월 15일은 {}입니다.".format(weekday_name))

#================================================================================================================
#numpy
#배열 생성
import numpy as np

# 1차원 배열 생성
a = np.array([1, 2, 3])
print(a)  # [1 2 3]

# 2차원 배열 생성
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b)
# [[1 2]
#  [3 4]
#  [5 6]]
#-----------------------------------------------------------------------------------------------------------------
#배열 연산
import numpy as np

# 배열 더하기
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)  # [5 7 9]

# 배열 곱하기
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b
print(c)  # [4 10 18]

# 행렬 곱셈
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)
print(c)
# [[19 22]
#  [43 50]]
#-----------------------------------------------------------------------------------------------------------------
# 배열 인덱싱과 슬라이싱
import numpy as np

# 배열 인덱싱
a = np.array([1, 2, 3, 4, 5])
print(a[0])  # 1
print(a[-1])  # 5

# 2차원 배열 인덱싱
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b[0, 1])  # 2

# 배열 슬라이싱
a = np.array([1, 2, 3, 4, 5])
print(a[1:4])  # [2 3 4]

# 2차원 배열 슬라이싱
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b[1:3, :]) 
# [[3 4]
#  [5 6]]


#-----------------------------------------------------------------------------------------------------------------
#배열 변형
import numpy as np

# 배열 크기 변경
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.reshape(a, (2, 3))
print(b)
# [[1 2 3]
#  [4 5 6]]

# 배열 전치
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.transpose(a)
print(b)
# [[1 3 5]
#  [2 4 6]]

#================================================================================================================
#pandas
import pandas as pd

# 시리즈(Series) 예시 : 1차원 행렬의 형태
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)

# 데이터프레임(DataFrame) 예시 : 표 안에 데이터가 들어가있는 형태(2차원 행렬의 형태)
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'year': [2017, 2017, 2018, 2019],
        'score': [100, 95, 80, 90]}
df = pd.DataFrame(data)
print(df)

# 데이터프레임에서 열 선택 예시
print(df['name'])
print(df.year)

# 조건을 이용한 데이터 선택 예시
print(df[df.year > 2017])

# 데이터프레임에 열 추가 예시
df['grade'] = ['A', 'A-', 'B+', 'B']
print(df)

# 데이터프레임에서 행 선택 예시
print(df.loc[0])
print(df.loc[[0, 2]])

# 데이터프레임에서 행과 열 선택 예시
print(df.loc[0, 'name'])
print(df.loc[[0, 2], ['name', 'score']])

#================================================================================================================
#matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(-np.pi, np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 그래프 그리기
plt.plot(x, y_sin, label='sin')
plt.plot(x, y_cos, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos Functions')
plt.legend()
plt.show()

