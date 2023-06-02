#0이 입력되기 전까지 입력 받은 양수 출력
while True:
    x = int(input("숫자를 입력하세요: "))
    if x == 0:
        break
    elif x < 0:
        print("잘못된 입력입니다.")
        pass
    else:
        print("입력한 숫자는 {}입니다.".format(x))

#입력 문자열에서 모음을 제거 후 출력
vowels = ['a', 'e', 'i', 'o', 'u']
input_str = input("Enter a string: ")

output_str = ""
for char in input_str:
    if char in vowels:
        pass
    else:
        output_str += char

print("Modified string:", output_str)

#숫자 맞추기
import random

# 1부터 100 사이의 임의의 수를 선택합니다
secret_number = random.randint(1, 100)

while True:
    # 사용자가 숫자를 입력합니다
    guess = int(input("Guess the secret number (between 1 and 100): "))

    # 입력한 숫자와 비교합니다
    if guess < secret_number:
        print("Up")
    elif guess > secret_number:
        print("Down")
    else:
        print("Correct!")
        break  # 정답을 맞추었으므로 반복문을 종료합니다


#1부터 100까지 정수 무작위 생성
import random

random_number = random.randint(1, 100)
print(random_number)

#리스트에서 무작위로 선택된 하나의 과일 출력
import random

fruits = ['apple', 'banana', 'orange', 'pear']
print(random.choice(fruits))

#리스트 항목을 무작위로 섞기
import random

cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
random.shuffle(cards)
print(cards)

#시퀀스 자료형에서 중복 없이 n개의 요소를 랜덤하게 뽑아 리스트로 반환하기
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_numbers = random.sample(numbers, 3)
print(random_numbers)

#무작위의 도시와 날씨를 출력하는 예제
import random

# 도시와 날씨 리스트 정의
cities = ['서울', '부산', '인천', '대구', '광주', '대전']
weathers = ['맑음', '흐림', '비', '눈', '우박']

# 도시와 날씨를 무작위로 선택하여 출력
city = random.choice(cities)
weather = random.choice(weathers)
print(f'{city}의 날씨는 {weather}입니다.')
