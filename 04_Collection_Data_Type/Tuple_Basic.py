# 빈 튜플 생성
t1 = ()
print(t1)  # ()

# 요소가 하나인 튜플은 요소 뒤에 콤마(,)를 붙여서 생성
t2 = (1,)
print(t2)  # (1,)

# 여러 요소를 가진 튜플 생성
t3 = (1, 2, 3)
print(t3)  # (1, 2, 3)

# 리스트나 문자열을 튜플로 변환
t4 = tuple([1, 2, 3])
print(t4)  # (1, 2, 3)

t5 = tuple("hello")
print(t5)  # ('h', 'e', 'l', 'l', 'o')

# 소괄호 없이도 생성 가능
t = 1, 2, 3
print(t)  # (1, 2, 3)

# 튜플 생성
my_tuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')

# 인덱싱
print(my_tuple[0])   # 'apple' 출력
print(my_tuple[-1])  # 'mango' 출력

# 슬라이싱
print(my_tuple[2:5])   # ('cherry', 'orange', 'kiwi') 출력
print(my_tuple[:4])    # ('apple', 'banana', 'cherry', 'orange') 출력
print(my_tuple[2:])    # ('cherry', 'orange', 'kiwi', 'melon', 'mango') 출력
print(my_tuple[::2])   # ('apple', 'cherry', 'kiwi', 'mango') 출력
print(my_tuple[::-1])  # ('mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple') 출력

#---------------------------------------------------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# 튜플 이어붙이기
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# 튜플 반복하기
tuple4 = tuple1 * 3
print(tuple4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

t = (1, 2, 3, 2, 4, 2)
#count(value): 튜플에서 해당 값이 등장하는 횟수를 반환합니다.
print(t.count(2))  # 3

#index(value): 튜플에서 해당 값이 처음으로 등장하는 인덱스를 반환합니다.
print(t.index(2))  # 1

#튜플 언패킹(tuple unpacking)은 튜플의 각 요소를 개별 변수로 할당하는 것을 말합니다.
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3

#튜플 언패킹을 이용하면 두 변수의 값을 쉽게 교환할 수 있습니다.
x = 1
y = 2
x, y = y, x
print(x)  # 2
print(y)  # 1

#튜플을 이용한 함수에서는 여러 값을 동시에 반환할 수 있으며, 함수의 매개변수로서 튜플을 사용하여 함수에 여러 인수를 전달할 수 있습니다.

def calculate(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = x / y
    return add, subtract, multiply, divide
