#numpy 배열 생성
import numpy as np

# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 2차원 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

# 배열 데이터 타입 지정
arr3 = np.array([1, 2, 3], dtype=float)
print(arr3)  # [1. 2. 3.]

#----------------------------------------------------------------------------------------------------------------------------

import numpy as np

# 3차원 배열 생성
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)

# 4차원 배열 생성
arr4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(arr4d)

#=============================================================================================================================
#arange 함수 : 지정된 범위 내에서 균일한 간격으로 값을 생성하여 1차원 배열을 반환하는 함수
#numpy.arange(start, stop, step, dtype=None)
# start: 시작 값으로, 범위에 포함됩니다. 기본값은 0입니다.
# stop: 종료 값으로, 범위에 포함되지 않습니다. 이 값을 생성하지 않습니다.
# step: 값 사이의 간격을 나타내며, 기본값은 1입니다.
# dtype: 생성된 배열의 데이터 유형을 지정합니다. 기본값은 입력 값에 따라 자동으로 결정됩니다.

import numpy as np

# 기본 사용법
arr1 = np.arange(5)
print(arr1) # 출력: [0 1 2 3 4]

#----------------------------------------------------------------------------------------------------------------------------
import numpy as np

# start, stop, step 지정
arr2 = np.arange(2, 10, 2)
print(arr2)
# 출력: [2 4 6 8]

# 부동 소수점 사용
arr3 = np.arange(0, 1, 0.1)
print(arr3)
# 출력: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

# dtype 지정
arr4 = np.arange(1, 6, dtype=np.float)
print(arr4) # 출력: [1. 2. 3. 4. 5.]

#=============================================================================================================================
# random.rand 함수 : 주어진 형상(shape)에 맞는 랜덤한 값을 가지는 배열을 생성하는 함수
# numpy.random.rand(d0, d1, ..., dn)
# d0, d1, ..., dn: 생성하려는 배열의 형상(shape)을 나타내는 인수들입니다. 각 인수는 해당 차원의 크기를 나타냅니다. 인수들은 정수로 지정되어야 합니다.
import numpy as np

# 1차원 배열
arr1 = np.random.rand(5)
print(arr1)
# 출력: [0.83958127 0.24040059 0.347213   0.84438691 0.40773203]

#----------------------------------------------------------------------------------------------------------------------------
import numpy as np

# 2차원 배열
arr2 = np.random.rand(3, 2)
print(arr2)
# 출력:
# [[0.19939998 0.75956173]
#  [0.01483635 0.53638077]
#  [0.87976498 0.97136662]]

# 3차원 배열
arr3 = np.random.rand(2, 2, 2)
print(arr3)
# 출력:
# [[[0.59316751 0.39113902]
#   [0.18339846 0.53238345]]
#
#  [[0.48801979 0.71909972]
#   [0.52657897 0.23042326]]]

#=============================================================================================================================
# random.normal 함수 : 정규 분포(가우시안 분포)를 따르는 난수를 생성하는 함수 / 지정된 평균과 표준 편차에 따라 난수를 생성
# numpy.random.normal(loc=0.0, scale=1.0, size=None)
# loc: 정규 분포의 평균 값입니다. 기본값은 0.0입니다.
# scale: 정규 분포의 표준 편차 값입니다. 기본값은 1.0입니다.
# size: 생성하려는 배열의 형상(shape)을 나타내는 인수입니다. 기본값은 None이며, 하나의 난수를 반환합니다.
import numpy as np

# 기본 사용법
arr1 = np.random.normal()
print(arr1)
# 출력: 난수 값 (예: -0.4530624371238927)

#----------------------------------------------------------------------------------------------------------------------------
import numpy as np

# 평균과 표준 편차 지정
arr2 = np.random.normal(loc=1.0, scale=2.0, size=(2, 3))
print(arr2)
# 출력:
# [[ 3.15326523  1.80904146  0.11287371]
#  [ 0.59920925 -0.47195788  0.35207441]]
# 평균이 1.0이고 표준 편차가 2.0인 2x3 배열을 생성

# 형상(shape) 지정
arr3 = np.random.normal(size=(4,))
print(arr3) # 출력: 크기가 4인 1차원 배열

#=============================================================================================================================
# linspace 함수 : 지정된 범위에서 균일한 간격으로 값을 생성하여 1차원 배열을 반환하는 함수 / 시작 값과 종료 값 사이에서 지정된 개수의 동일한 간격으로 값을 생성
#numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# start: 시작 값으로, 범위에 포함됩니다.
# stop: 종료 값으로, 범위에 포함됩니다.
# num: 생성하려는 값의 개수입니다. 기본값은 50입니다.
# endpoint: 종료 값이 결과에 포함되는지 여부를 나타내는 부울 값입니다. 기본값은 True이며, True인 경우 종료 값이 결과에 포함됩니다.
# retstep: 반환된 값 중 간격(step) 값을 함께 반환할지 여부를 나타내는 부울 값입니다. 기본값은 False이며, True로 설정하면 간격(step) 값을 함께 반환합니다.
# dtype: 생성된 배열의 데이터 유형을 지정합니다. 기본값은 입력 값에 따라 자동으로 결정됩니다.

import numpy as np

# 기본 사용법
arr1 = np.linspace(0, 1, num=5)
print(arr1)
# 출력: [0.   0.25 0.5  0.75 1.  ]

# 개수와 간격 확인
arr2, step = np.linspace(0, 1, num=5, retstep=True)
print(arr2)
# 출력: [0.   0.25 0.5  0.75 1.  ]
print(step)
# 출력: 0.25

# 종료 값 포함하지 않음
arr3 = np.linspace(0, 10, num=5, endpoint=False)
print(arr3)
# 출력: [0. 2. 4. 6. 8.]

# 데이터 유형 지정
arr4 = np.linspace(1, 5, num=5, dtype=np.int)
print(arr4)
# 출력: [1 2 3 4 5]

#=============================================================================================================================
# Matplotlib : 파이썬에서 데이터 시각화를 위한 가장 일반적인 라이브러리. 다양한 유형의 그래프를 그리는 데 사용 가능.
# Matplotlib은 파이썬의 기본 라이브러리인 NumPy와 함께 사용.

# 선 그래프
# color: 그래프 색상
# linestyle: 선 스타일 (solid, dashed, dotted, dashdot 등)
# linewidth: 선 굵기
# marker: 마커 스타일 (circle, square, triangle 등)
# markersize: 마커 크기
# 선 그래프 스타일 변경 : plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markersize=5)
import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 선 그래프 그리기
plt.plot(x, y)

# 그래프 타이틀과 축 라벨 설정
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()


#----------------------------------------------------------------------------------------------------------------------------
#산점도 : 점으로 그래프 그리기
# color: 마커 색상
# marker: 마커 스타일 (circle, square, triangle 등)
# s: 마커 크기
# alpha: 마커 투명도
# 산점도 스타일 변경 : plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)

import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
plt.scatter(x, y)

# 그래프 타이틀과 축 라벨 설정
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
#색상 변경
# 'b': 파란색 (blue)
# 'g': 초록색 (green)
# 'r': 빨간색 (red)
# 'c': 청록색 (cyan)
# 'm': 자홍색 (magenta)
# 'y': 노란색 (yellow)
# 'k': 검정색 (black)
# 'w': 흰색 (white)

import matplotlib.pyplot as plt
import numpy as np

# 색상 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='#FF5733')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 라인 스타일 변경
# 'solid': 실선
# 'dashed': 파선
# 'dashdot': 점선과 파선 번갈아가며
# 'dotted': 점선

import matplotlib.pyplot as plt
import numpy as np

# 라인 스타일 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed')
plt.plot(x, y2, linestyle='dashdot')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 마커 변경
# '.' : 작은 점 (point)
# ',' : 픽셀 (pixel)
# 'o' : 원 (circle)
# 'v' : 역삼각형 (triangle_down)
# '^' : 삼각형 (triangle_up)
# '<' : 왼쪽 화살표 (triangle_left)
# '>' : 오른쪽 화살표 (triangle_right)
# '1' : 아래쪽으로 뾰족한 별 (tri_down)
# '2' : 위쪽으로 뾰족한 별 (tri_up)
# '3' : 왼쪽으로 뾰족한 별 (tri_left)
# '4' : 오른쪽으로 뾰족한 별 (tri_right)
# 's' : 네모 (square)
# 'p' : 오각형 (pentagon)
# '*' : 별표 (star)
# 'h' : 육각형1 (hexagon1)
# 'H' : 육각형2 (hexagon2)
# '+' : 플러스 (plus)
# 'x' : 엑스 (x)
# 'D' : 다이아몬드 (diamond)
# 'd' : 작은 다이아몬드 (thin_diamond)
# '|' : 수직선 (vline)
# '_' : 수평선 (hline)

import matplotlib.pyplot as plt
import numpy as np

# 마커 변경 예제
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, marker='^')
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 범례 추가
# 'best': 자동으로 최적의 위치를 선택합니다.
# 'upper right': 오른쪽 상단에 위치합니다.
# 'upper left': 왼쪽 상단에 위치합니다.
# 'lower right': 오른쪽 하단에 위치합니다.
# 'lower left': 왼쪽 하단에 위치합니다.
# 'right': 오른쪽에 위치합니다.
# 'center left': 중앙 왼쪽에 위치합니다.
# 'center right': 중앙 오른쪽에 위치합니다.
# 'lower center': 하단 중앙에 위치합니다.
# 'upper center': 상단 중앙에 위치합니다.
# 'center': 중앙에 위치합니다.
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed', label='Sine')
plt.plot(x, y2, linestyle='dashdot', label='Cosine')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right', fontsize=12, shadow=True, title='Legend')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 스타일 적용 : plt.style.context() 함수를 사용하여 각 스타일을 적용할 수 있습니다.
import matplotlib.pyplot as plt
import numpy as np

# 스타일 리스트
styles = ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale', 'Solarize_Light2', 'tableau-colorblind10']

# 스타일 적용 예제
for style in styles:
    plt.style.use(style)
    x = np.arange(0, 10, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label='Sine')
    plt.plot(x, y2, label='Cosine')
    plt.title('Sine and Cosine Waves')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# subplot : 다양한 크기의 서브플롯을 생성, 생성된 서브플롯은 index위치에 생성 (동일한 크기로 자름)
# 그래프 창을 격자(grid) 형태로 나누어 각 위치에 그래프를 그리기
plt.subplot(rows, cols, index)
# rows: 그리드의 행(row) 개수
# cols: 그리드의 열(column) 개수
# index: 현재 서브플롯의 위치를 나타내는 숫자


import matplotlib.pyplot as plt

# 그리드 설정
fig = plt.figure()

ax1 = plt.subplot(1, 3, 1)
ax1.plot([1, 2, 3, 4], [1, 4, 2, 3])

ax2 = plt.subplot(2, 3, 2)
ax2.plot([1, 2, 3, 4], [1, 4, 2, 3])

ax3 = plt.subplot(2, 3, 5)
ax3.plot([1, 2, 3, 4], [1, 4, 2, 3])

ax4 = plt.subplot(1, 3, 3)
ax4.plot([1, 2, 3, 4], [1, 4, 2, 3])

# 그래프 표시
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# subplots 함수 : 단순히 격자 형태로 동일한 크기의 서브플롯을 생성하기 위해 사용
fig, axes = plt.subplots(rows, cols)
# rows: 그리드의 행(row) 개수
# cols: 그리드의 열(column) 개수
# fig: 그래프 창을 나타내는 Figure 객체
# axes: 서브플롯을 나타내는 Axes 객체(또는 Axes 객체의 배열)
# index: 현재 서브플롯의 위치를 나타내는 숫자

import matplotlib.pyplot as plt
import numpy as np

# 2x2 서브플롯 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 2x2 서브플롯 생성
fig, axs = plt.subplots(2, 2, figsize=(8, 8)) #(2.2) 배열을 생성하여 그래프 총 4개 삽입

# 첫 번째 서브플롯
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine')

# 두 번째 서브플롯
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine')

# 세 번째 서브플롯
axs[1, 0].plot(x, y1 + y2)
axs[1, 0].set_title('Sine + Cosine')

# 네 번째 서브플롯
axs[1, 1].plot(x, y1 - y2)
axs[1, 1].set_title('Sine - Cosine')

plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# subplot2grid : 더 세밀하게 서브플롯을 배치할 수 있음
plt.subplot2grid(shape, loc, rowspan=1, colspan=1)
# shape: 그리드의 모양을 나타내는 튜플 (rows, cols)
    # rows는 그리드의 행(row) 개수
    # cols는 그리드의 열(column) 개수
# loc: 현재 서브플롯의 위치를 나타내는 튜플 (row, col)
    # row: 현재 서브플롯의 행 인덱스
    # col: 현재 서브플롯의 열 인덱스
# rowspan: 현재 서브플롯이 차지할 행(row) 개수를 나타냅니다. 기본값은 1
# colspan: 현재 서브플롯이 차지할 열(column) 개수를 나타냅니다. 기본값은 1
import matplotlib.pyplot as plt

# 그리드 설정
fig = plt.figure()

# 첫 번째 서브플롯 (3x3 그리드의 (0, 0) 위치, 열 3칸 차지)
ax1 = plt.subplot2grid((3, 3), (0, 0), 1, 3) #1행3열짜리 그래프의 크기를 선택
ax1.plot([1, 2, 3, 4], [1, 4, 2, 3])

# 두 번째 서브플롯 (3x3 그리드의 (1, 0) 위치, 열 2칸 차지)
ax2 = plt.subplot2grid((3, 3), (1, 0), 1,2)
ax2.plot([1, 2, 3, 4], [1, 4, 2, 3])

# 세 번째 서브플롯 (3x3 그리드의 (1, 2) 위치, 행 2 칸 차지)
ax3 = plt.subplot2grid((3, 3), (1, 2), 2, 1)
ax3.plot([1, 2, 3, 4], [1, 4, 2, 3])

# 네 번째 서브플롯 (3x3 그리드의 (2, 0) 위치, 열 2 칸 차지)
ax4 = plt.subplot2grid((3, 3), (2, 0), 1, 2)
ax4.plot([1, 2, 3, 4], [1, 4, 2, 3])

# 그래프 간격 조정
plt.tight_layout()

# 그래프 표시
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 막대 그래프(Bar plot) : 막대 그래프는 범주형 데이터를 시각화하는 데 자주 사용됩니다. x축에는 범주형 변수, y축에는 연속형 변수를 사용하여 표시합니다.
import matplotlib.pyplot as plt
import numpy as np

labels = ['apple', 'banana', 'orange', 'grape', 'kiwi']
values = [20, 10, 15, 25, 30]

plt.bar(labels, values)
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 히스토그램 (Histogram) : 히스토그램은 데이터의 분포를 나타내는 데 자주 사용됩니다. 데이터를 구간으로 나누고, 각 구간에 속하는 데이터의 개수를 세어서 표시합니다.
import matplotlib.pyplot as plt
import numpy as np

data = np .random.normal(0, 1, 1000)

plt.hist(data)
plt.show()

#----------------------------------------------------------------------------------------------------------------------------
# 히트맵 (Heatmap) : 히트맵은 데이터의 상관 관계를 나타내는 데 자주 사용됩니다. 색상을 사용하여 데이터 값의 크기를 나타냅니다.
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

plt.imshow(data, cmap='hot', interpolation='nearest')# imshow(): 2차원 배열을 이미지로 변환하여 표시 # cmap: 매개변수를 사용하여 색상 맵을 지정
plt.colorbar() #colorbar(): 색상 막대기를 추가
plt.show()


#----------------------------------------------------------------------------------------------------------------------------
# 등고선 그래프 (Contour plot) : 등고선 그래프는 2차원 함수의 등고선을 나타내는 데 자주 사용됩니다.
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z)
plt.show()


#=============================================================================================================================
#배열
#배열 인덱싱
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 인덱스가 0부터 시작하므로 arr[0]은 첫번째 요소를 의미함
print(arr[0])  # 1

# 음수 인덱스를 사용하면 배열의 끝부터 요소를 선택할 수 있음
print(arr[-1])  # 5

# 다차원 배열의 인덱싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])  # 1
print(arr2d[1, 1])  # 5

#----------------------------------------------------------------------------------------------------------------------------
# 배열 슬라이싱
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 슬라이싱은 [시작:끝:간격] 형식으로 사용
print(arr[1:4])  # [2 3 4]

# 다차원 배열의 슬라이싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0:2, 1:3])
'''
[[2 3]
 [5 6]]
'''

# 모든 행을 선택할 때는 ':'만 사용 가능
print(arr2d[:, 1])
'''
[2 5 8]
'''


#----------------------------------------------------------------------------------------------------------------------------
# 부울린 인덱싱
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = np.array([True, False, True, False, True])

# mask 배열에 True에 해당하는 인덱스의 요소만 선택
print(arr[mask])  # [1 3 5]


#----------------------------------------------------------------------------------------------------------------------------
# 팬시 인덱싱 : 배열에 인덱스 배열을 전달하여 배열의 원하는 요소를 선택하는 방법
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
idx = np.array([0, 2, 4])

# 인덱스 배열에 해당하는 요소만 선택
print(arr[idx])  # [1 3 5]

# 다차원 배열에서의 팬시 인덱싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_idx = np.array([0, 2])
col_idx = np.array([1, 2])

# 인덱스 배열로 선택된 요소만 선택
print(arr2d[row_idx, col_idx])  # [2 9]


#----------------------------------------------------------------------------------------------------------------------------
#배열 연산
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 덧셈 연산
print(arr1 + arr2)  # [5 7 9]

# 뺄셈 연산
print(arr1 - arr2)  # [-3 -3 -3]

# 곱셈 연산
print(arr1 * arr2)  # [ 4 10 18]

# 나눗셈 연산
print(arr1 / arr2)  # [0.25 0.4  0.5]

#----------------------------------------------------------------------------------------------------------------------------
#브로드캐스팅 : NumPy에서 크기가 다른 배열 간의 연산을 가능하게 해주는 기능입니다. 브로드캐스팅은 작은 배열을 자동으로 확장하여 큰 배열에 맞추어 연산을 수행합니다.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1])
arr3 = np.array([[1],[2],[3]])


# 브로드캐스팅을 통해 크기가 다른 배열 간 연산이 가능
print(arr1 + arr2)
print(arr1 + arr3)

#----------------------------------------------------------------------------------------------------------------------------
# 유니버설 함수 :  배열의 요소(element)에 대해 적용되는 함수를 말하며, 배열의 각 요소에 대해 한 번에 계산이 가능합니다.
import numpy as np

arr = np.array([0, 1, 2, 3, 4])

print(np.sqrt(arr))  # [0.         1.         1.41421356 1.73205081 2.        ]
print(np.exp(arr))  # [ 1.          2.71828183  7.3890561  20.08553692 54.59815003]
print(np.log(arr+1))  # [0.         0.69314718 1.09861229 1.38629436 1.60943791]

#----------------------------------------------------------------------------------------------------------------------------
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 배열의 요소에 대해 적용되는 함수
print(np.add(arr1, arr2))  # [5 7 9]
print(np.multiply(arr1, arr2))  # [ 4 10 18]
print(np.power(arr1, arr2))  # [   1   32  729]


#----------------------------------------------------------------------------------------------------------------------------
# 배열 형태, 구조 변경
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# 배열 형태 변경
arr2d = arr.reshape((2, 4))
print(arr2d)

# 배열 구조 변경
arr2d_reshape = arr2d.reshape(4, 2)
print(arr2d_reshape)

# 배열 전치(Transpose)
arr2d_transpose = arr2d.T
print(arr2d_transpose)


#----------------------------------------------------------------------------------------------------------------------------
# 배열 합치기, 분할하기
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# 수직 합치기
print(np.vstack((arr1, arr2)))

# 수평 합치기
print(np.hstack((arr1, arr2)))

# 배열 분할하기
arr3 = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr3, 3))

# 다차원 배열 분할하기
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.vsplit(arr4, 3))

#----------------------------------------------------------------------------------------------------------------------------
# 통계 및 수학 함수
# 통계 함수
import numpy as np

# 1차원 배열 생성
arr = np.array([1, 2, 3, 4, 5])

# 평균 계산
print(np.mean(arr))  # 3.0

# 중앙값 계산
print(np.median(arr))  # 3.0

# 표준편차 계산
print(np.std(arr))  # 1.4142135623730951

# 분산 계산
print(np.var(arr))  # 2.0

# 최대값, 최소값 계산
print(np.max(arr))  # 5
print(np.min(arr))  # 1

# 정규분포
numpy.random.normal(loc=0.0, scale=1.0, size=None)
# loc: 정규 분포의 평균값, scale: 표준편차, size: 생성할 난수의 개수
import numpy as np

arr1 = np.random.normal(0, 1, size=10)
print(arr1)


# 균등분포
numpy.random.uniform(low=0.0, high=1.0, size=None)
# low와 high: 균등 분포의 최솟값과 최댓값, size: 생성할 난수의 개수
import numpy as np

arr2 = np.random.uniform(0, 1, size=10)
print(arr2)


# 이항분포
numpy.random.binomial(n, p, size=None)
# n: 베르누이 시행을 반복하는 횟수, p: 각 시행에서의 성공 확률, size는 생성할 난수의 개수
import numpy as np

arr3 = np.random.binomial(10, 0.5, size=10)
print(arr3)

# 포아송 분포
numpy.random.poisson(lam=1.0, size=None)
# lam: 단위 시간 또는 공간에서 발생하는 사건의 평균 개수, size: 생성할 난수의 개수
import numpy as np

arr4 = np.random.poisson(3, size=10)
print(arr4)


#=============================================================================================================================
#파일 입출력
# NumPy 배열을 파일로 저장하고 읽어오기
import numpy as np

# 단일 배열 저장
arr1 = np.array([1, 2, 3, 4, 5])
np.save('arr1.npy', arr1)

# 다중 배열 저장
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([10, 20, 30, 40, 50])
np.savez('arr.npz', arr2=arr2, arr3=arr3)

# 배열 불러오기
loaded_arr1 = np.load('arr1.npy')
loaded_data = np.load('arr.npz')
loaded_arr2 = loaded_data['arr2']
loaded_arr3 = loaded_data['arr3']
