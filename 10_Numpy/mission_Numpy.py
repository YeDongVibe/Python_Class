# Graph
# 임의의 판매 실적 데이터를 생성하고, 이를 이용하여 그래프를 그리는 예제
# months = np.arange(1, 13)  # 월별 데이터
# sales = np.array([120, 145, 98, 156, 104, 176, 155, 140, 135, 120, 148, 170])  # 월별 판매량
import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)  # 월별 데이터
sales = np.array([120, 145, 98, 156, 104, 176, 155, 140, 135, 120, 148, 170])  # 월별 판매량

plt.plot(months, sales, marker='o',color='blue')
plt.grid()

plt.title('Monthly Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()
#----------------------------------------------------------------------------------------------------------------------------
# 두 가지 판매 물건의 실적 데이터를 생성하고, 이를 이용하여 그래프를 그리는 예제
# months = np.arange(1, 13)  # 월별 데이터
# product1_sales = np.array([120, 145, 98, 156, 104, 176, 155, 140, 135, 120, 148, 170])  # 물건 1 월별 판매량
# product2_sales = np.array([90, 110, 80, 120, 105, 140, 130, 125, 115, 100, 130, 150])  # 물건 2 월별 판매량
import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)  # 월별 데이터
product1_sales = np.array([120, 145, 98, 156, 104, 176, 155, 140, 135, 120, 148, 170])  # 물건 1 월별 판매량
product2_sales = np.array([90, 110, 80, 120, 105, 140, 130, 125, 115, 100, 130, 150])  # 물건 2 월별 판매량

plt.plot(months, product1_sales, marker='o',color='blue', label = 'Product1')
plt.plot(months, product2_sales, marker='o',color='red', label = 'Product2')
plt.grid(True)
plt.legend(loc = 'upper left', fontsize=12, shadow=True)

plt.title('Monthly Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()
#----------------------------------------------------------------------------------------------------------------------------
# 각 나라별 GDP 비교 그래프를 그리는 예제
# years = np.arange(2010, 2021)  # 연도 데이터
# gdp_a = np.array([100, 120, 150, 160, 180, 200, 220, 240, 260, 280, 300])  # A 나라의 연도별 GDP
# gdp_b = np.array([80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])  # B 나라의 연도별 GDP
# gdp_c = np.array([200, 220, 240, 250, 260, 270, 280, 290, 300, 310, 320])  # C 나라의 연도별 GDP
import matplotlib.pyplot as plt
import numpy as np


years = np.arange(2010, 2021)  # 연도 데이터
gdp_a = np.array([100, 120, 150, 160, 180, 200, 220, 240, 260, 280, 300])  # A 나라의 연도별 GDP
gdp_b = np.array([80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])  # B 나라의 연도별 GDP
gdp_c = np.array([200, 220, 240, 250, 260, 270, 280, 290, 300, 310, 320])  # C 나라의 연도별 GDP

w = 0.25
index = np.arange(len(years))

plt.bar(index-w, gdp_a, width=w, color='blue', label = 'Country A')
plt.bar(index, gdp_b, width=w, color='red', label = 'Country B')
plt.bar(index+w, gdp_c, width=w, color='green', label = 'Country C')

plt.xticks(index, years) #index위치에 years 값을 넣어라
plt.xlabel('years')
plt.ylabel('GDP')
plt.grid()
plt.legend(loc = 'upper left', fontsize=12, shadow=True)
plt.show()
#----------------------------------------------------------------------------------------------------------------------------
# 그래프 창을 다양한 크기로 구성하여 그래프 그리는 예제
# years = np.arange(2010, 2021)
# gdp = np.array([100, 120, 150, 160, 180, 200, 220, 240, 260, 280, 300])
# sales = np.array([50, 70, 30, 45, 60, 80, 70, 90, 110, 100, 120])
# prices = np.array([10, 12, 15, 16, 18, 20, 22, 24, 26, 28, 30])
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

years = np.arange(2010, 2021)
gdp = np.array([100, 120, 150, 160, 180, 200, 220, 240, 260, 280, 300])
sales = np.array([50, 70, 30, 45, 60, 80, 70, 90, 110, 100, 120])
prices = np.array([10, 12, 15, 16, 18, 20, 22, 24, 26, 28, 30])

ax1 = plt.subplot2grid((3, 3), (0, 0), 1, 3)
ax1.plot(years, gdp, marker='o',color='blue')
ax1.set_title('GDP')
ax1.set_ylabel('GDP')

ax2 = plt.subplot2grid((3, 3), (1, 0), 1, 2)
ax2.bar(years, sales, color = 'green')
ax2.set_title('Sales')
ax2.set_ylabel('Quantity Sold')

ax3 = plt.subplot2grid((3, 3), (1, 2), 2, 1)
ax3.scatter(years, prices, color = 'red')
ax3.set_title('Prices')
ax3.set_ylabel('Price')

ax4 = plt.subplot2grid((3, 3), (2, 0), 1, 2)
ax4.plot(years, sales, marker='o',color='blue')
ax4.set_title('Sales')
ax4.set_ylabel('Quantity Sold')

plt.tight_layout()
plt.show()


#=============================================================================================================================