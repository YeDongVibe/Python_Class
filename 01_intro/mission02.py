#사과사과
num1 = int(input("사과의 갯수를 말하라 오바."))
num2 = int(input("사과의 가격을 말하라 오바."))
num3 = 0.9
result = (num1*num2)*(1.1)

print(f"총 가격은 {result}이다.\n")

#초
num1 = int(input("몇초임?"))

min = num1/60
sec = num1%60

print(f"{num1}초는 {min:.0f}분 {sec}초 여.\n")

#시간변환
num1 = int(input("몇 분임?"))

day = num1//(60*24)
hour = (num1 // 60) % 24
min = num1%60

print(f"{num1}는 {day}일 {hour}시간 {min}분 임.\n")

#금리
result = 500 * (1 + (0.05)**5)

print(f"원금리 합계는  {result}입니다.\n")

#연속 된 숫자 합
result = (100 * 101) / 2

print(f"총 합은{result}입니다.\n")

#총 무게
num1 = int(input("포도 알 개수는?"))
num2 = int(input("딸기 알 개수는?"))

result = (num1*75) + (num2*113.5)

print(f"총 무게는 {result}입니다.\n")