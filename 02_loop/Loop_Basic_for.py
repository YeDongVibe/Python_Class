# 리스트 원소를 순차적으로 출력
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#리스트에 저장 된 수의 합을 출력
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)

#튜플<소괄호()를 이용한 배열?>의 원소를 순차적으로 출력
colors = ("red", "green", "blue")

for color in colors:
    print(color)

#문자열의 각 문자를 순차적으로 출력
text = "Python"

for char in text:
    print(char)

#1부터 10까지의 숫자 출력
for i in range(1, 11):
    print(i)

#1부터 10까지의 숫자 중 짝수만 출력
for i in range(2, 11, 2):
    print(i)

#1부터 10까지의 숫자 역순으로 출력
for i in range(10, 0, -1):
    print(i)
