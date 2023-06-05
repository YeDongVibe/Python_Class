# 함수 정의
def add_numbers(a, b):
    result = a + b
    return result

# 함수 호출
result = add_numbers(3, 5)
print(result)   # 출력 결과: 8

#반환 값이 없는 함수
def prtStr(str) :   	   #str을 매개변수라 함
    print("%s" %str)
    return              #반환 값이 없이 함수가 종료

str = "Wecome to Python"
prtStr(str)             #매개변수를 전달하여 함수 호출

#값을 반환하는 함수
def squareArea(s) :
    area = s * s
    return area           #area 값이 반환되고 종료

a = squareArea(5)    #5를 인자(argument)라 함. 반환 값이 a에 저장
b = squareArea(7)
print("한변의 길이가 %d인 정사각형의 넓이는 %d" %(5, a))
print("한변의 길이가 %d인 정사각형의 넓이는 %d" %(7, b))

# 위치 인자와 키워드 인자 사용 예시
def print_info(name, age, gender):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")

# 위치 인자를 사용하여 함수 호출
print_info("Alice", 25, "Female")

# 키워드 인자를 사용하여 함수 호출
print_info(age=30, name="Bob", gender="Male")

# 가변 인자와 기본값 인자 사용 예시
def print_numbers(*args, sep=", "):
    print(sep.join(map(str, args)))

# 가변 인자를 사용하여 함수 호출
print_numbers(1, 2, 3)               # 출력 결과: 1, 2, 3
print_numbers(1, 2, 3, sep="-")      # 출력 결과: 1-2-3

# 기본값 인자를 사용하여 함수 호출
def say_hello(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

say_hello("Alice")                  # 출력 결과: Hello, Alice!
say_hello("Bob", "Hi")              # 출력 결과: Hi, Bob!

# 인자의 순서와 조합 사용 예시
def print_numbers(a, b, *args, c=10, d=20): #a,b : 위치인자 / *args : 가변인자 / c,d : 기본인자가 수정되어 들어감
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"args: {args}")

# 함수 호출
print_numbers(1, 2, 3, 4, 5, c=30, d=40)
# 출력 결과: a: 1, b: 2, c: 30, d: 40, args: (3, 4, 5)

#변수 ----------------------------------------------------------------------------------------
x = 1  # 전역 변수

def my_function():
    y = 2  # 지역 변수
    print('y:', y)
    print('x:', x)

my_function()
print('x:', x)

#---------------------------------------------------------------------------------------------------------
x = 'global'

def my_function():
    global x
    x = 'local'

my_function()
print(x)

#pass 키워드
#함수 몸체의 작성을 잠시 보류할 때 사용
#문법적 오류를 피하고 아무 것도 실행하지 않을 때 사용 
def func(arg): 
    pass

#---------------------------------------------------------------------------------------------------------
#lambda 함수<lambda 인자: 표현식>
# 기존 함수 정의 방법
def add(a, b):
    return a + b

# 람다 함수 정의 방법 (함수가 변수에 할당가능)
lambda_add = lambda a, b: a + b

# 함수 호출
result1 = add(3, 4)             # 7
result2 = lambda_add(3, 4)      # 7
students = [
    {'name': 'Alice', 'score': 80},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 70},
]

# 점수(score)를 기준으로 학생 리스트 정렬
sorted_students = sorted(students, key=lambda student: student['score'], reverse=True) #reverse=True : 내림차순으로 진행하겠다
print(sorted_students)
# 출력 결과: [{'name': 'Bob', 'score': 90}, {'name': 'Alice', 'score': 80}, {'name': 'Charlie', 'score': 70}]

#함수의 반환값으로 사용 예시
def get_operator(operator):
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '-':
        return lambda a, b: a - b
    elif operator == '*':
        return lambda a, b: a * b
    elif operator == '/':
        return lambda a, b: a / b

# 함수의 반환값으로 람다 함수 사용
add_func = get_operator('+')
result1 = add_func(3, 4)  # 7

multiply_func = get_operator('*')
result2 = multiply_func(3, 4)  # 12

#재귀함수(Recursive Function)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)  # 출력결과: 120
