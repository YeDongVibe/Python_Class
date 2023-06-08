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


#내부 함수(inner function) <내부 함수는 외부 함수의 매개변수와 지역변수에 접근할 수 있다.>
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

result = outer_func(10)
print(result(20))  # 출력결과: 30

#계산기 함수
def calculator(): # 외부 함수
    def add(a, b): # 내부 함수
        return a + b

    def subtract(a, b): # 내부 함수
        return a - b

    def multiply(a, b): # 내부 함수
        return a * b

    def divide(a, b): # 내부 함수
        return a / b

    return add, subtract, multiply, divide # 튜플이 됨.

add, subtract, multiply, divide = calculator() #unpacking

print(add(10, 20))  # 출력결과: 30
print(subtract(10, 20))  # 출력결과: -10
print(multiply(10, 20))  # 출력결과: 200
print(divide(10, 20))  # 출력결과: 0.5

#제곱 함수
def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)  # 제곱 함수를 구현
cube = power(3)  # 세제곱 함수를 구현

print(square(3))  # 출력결과: 9
print(cube(3))  # 출력결과: 27

#---------------------------------------------------------------------------------------------------------
#일급 객체
#파이썬에서 함수는 일급 객체로 취급됩니다. 즉, 함수는 변수에 할당될 수 있고, 함수의 인자로 전달될 수 있으며, 함수의 반환값으로 사용될 수 있습니다.

#변수에 함수 할당하기
def add(a, b):
    return a + b
# 함수를 변수에 할당
func = add
# 변수에 할당된 함수 사용
result = func(3, 4)  # 7


#함수의 인자로 함수 전달하기
def calculate(func, a, b):
    return func(a, b)
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b

# 함수를 다른 함수의 인자로 전달
result1 = calculate(add, 3, 4)       # 7
result2 = calculate(multiply, 3, 4)  # 12


#함수의 반환값으로 함수 사용하기
def get_operator(operator):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b 
    def multiply(a, b):
        return a * b   
    def divide(a, b):
        return a / b
       
    if operator == '+':
        return add
    elif operator == '-':
        return subtract
    elif operator == '*':
        return multiply
    elif operator == '/':
        return divide
# 함수의 반환값으로 함수 사용
add_func = get_operator('+')
result = add_func(3, 4)  # 7


#---------------------------------------------------------------------------------------------------------
#가변 인자 
#파이썬에서는 가변 인자(*args, **kwargs)를 쉽게 처리할 수 있습니다. 이를 통해 함수가 받는 인자의 개수를 동적으로 조절할 수 있습니다.

 # *args를 이용한 가변 인자 처리
def sum_numbers(*args): # *args는 위치 인자(positional argument)를 가변적으로 처리하기 위한 구문 / 함수 내부에서는 튜플(tuple)<()> 형태로 처리
    result = 0
    for arg in args:
        result += arg
    return result
# 가변 인자를 사용하여 함수 호출
result1 = sum_numbers(1, 2, 3, 4, 5)   # 15
result2 = sum_numbers(1, 2, 3)         # 6
result3 = sum_numbers(1, 2)            # 3


# **kwargs를 이용한 가변 인자 처리
def print_info(**kwargs): # **kwargs는 키워드 인자(keyword argument)를 가변적으로 처리하기 위한 구문 / 함수 내부에서는 딕셔너리(dictionary)<{}> 형태로 처리.
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# 가변 키워드 인자를 사용하여 함수 호출
print_info(name='Alice', age=25, country='USA')
# 출력 결과: 
# name: Alice
# age: 25
# country: USA

#---------------------------------------------------------------------------------------------------------
#람다 함수
#파이썬에서는 람다(lambda) 함수를 지원합니다. 람다 함수는 함수를 간단하게 작성할 수 있어 코드의 가독성과 유연성을 높일 수 있습니다.
# 95번째 줄 참고

#---------------------------------------------------------------------------------------------------------
#디폴트 인자 값
#파이썬에서는 함수의 인자에 디폴트 값을 지정할 수 있습니다. 이를 통해 함수를 호출할 때 인자를 생략하면 디폴트 값이 사용되도록 할 수 있습니다.

#---------------------------------------------------------------------------------------------------------
#반환값 없음(None) : None은 파이썬에서 "값이 없음"을 나타내는 내장 객체
#파이썬에서는 함수가 반환값을 명시하지 않으면 자동으로 None 값을 반환합니다.
def print_greeting(name):
    print(f"Hello, {name}!")

# 함수 호출
result = print_greeting("Alice")   # 출력 결과: Hello, Alice!
print(result)                      # 출력 결과: None

#---------------------------------------------------------------------------------------------------------
#함수 내 변수 참조 순서
#Local -> Enclosing -> Global -> Built-in
#L (Local) : 함수 내부의 지역 변수입니다.
#E (Enclosing) : 함수를 포함하는 다른 함수(중첩 함수) 내부의 변수입니다.
#G (Global) : 전역 변수입니다.
#B (Built-in) : 내장 함수나 모듈 등 파이썬이 기본적으로 제공하는 것들입니다.

x = 'global' #전역변수 G

def outer():
    x = 'outer' #outer의 지역변수 L

    def inner():
        x = 'inner' #inner의 지역변수 L / outer의 입장에서 E
        print('x in inner:', x)   

    inner()
    print('x in outer:', x)

outer()
print('x in global:', x)


#---------------------------------------------------------------------------------------------------------
#내장 함수(Python이 제공하는 함수)
#bin(x), oct(x), hex(x) : 10진 정수 x에 대한 2진수, 8진수, 16진수 문자열 반환
#int(str, base=10) : 문자열 str을 10진수로 변환
bin(12)   #'0b1100'
int('123') #123
int('1010', 2) #10

#enumerate(iterable,start=0) : 주로 순서가 있는 자료형(리스트<[]>, 튜플<()> 등)의 각 요소에 대해 인덱스와 값을 동시에 반환하는데 사용
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)

#eval(expr,[globals[,locals]]) : 문자열로 표시된 파이썬 코드를 실행하고 결과를 반환
result = eval('2 + 3 * 4')
print(result)  # 출력 결과: 14

#filter(func,seq) : 시퀀스의 각 요소에 대해 함수를 적용하여 결과가 True인 것만 모아서 리스트<[]>로 반환하는 함수
#리스트에서 짝수만 추출하는 예시
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 출력 결과: [2, 4, 6, 8, 10]

#map(함수, 시퀀스) : 시퀀스의 각 원소에 대해 지정된 함수를 적용하여, 새로운 리스트<[]>를 반환
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # 출력결과: [1, 4, 9, 16, 25]

#ord(ch) : ch에 대한 ASCII 코드 반환
ord('A') #65

#repr(obj) : obj를 문자열로 변환
repr(b'0011') # "b'0011'"

#round(x, n=0) : 실수 x를 소수점 아래 n자리로 반올림하여 반환
num1 = 3.141592653589793238
num2 = 2.71828182845904523536

result1 = round(num1)    # 반올림하여 정수로 변환
result2 = round(num2, 3) # 소수점 셋째자리까지 반올림

print(result1) # 출력 결과: 3
print(result2) # 출력 결과: 2.718

#zip(seq, *seqs) : seq 요소와 *seqs 요소의 튜플 쌍으로 이루어진 리스트 iterable 반환
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 32, 28]

for name, age in zip(names, ages):
    print(name, age)
