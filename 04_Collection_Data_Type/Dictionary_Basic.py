#딕셔너리의 생성
# 빈 딕셔너리 생성
empty_dict = {}

# 문자열과 숫자로 이루어진 딕셔너리 생성
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# 다양한 타입으로 이루어진 딕셔너리 생성
mixed_dict = {'name': 'John', 'age': 25, 3: 'three', (1, 2): 'tuple'}

#딕셔너리는 키(key)를 사용하여 값을 가져올 수 있습니다.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # 'Alice'
print(my_dict['phone'])  # KeyError

#KeyError를 방지하고자 key가 딕셔너리에 있는지 먼저 확인한 후에 접근하는 것이 좋습니다.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
if 'name' in my_dict:
    print(my_dict['name'])  # 'Alice'
if 'phone' in my_dict:
    print(my_dict['phone'])  # 실행되지 않음

#요소 수정
# 딕셔너리 생성
person = {"name": "Alice", "age": 25, "gender": "female"}

# "name" 키의 값을 "Bob"으로 수정
person["name"] = "Bob"

# 딕셔너리 출력
print(person)  # {"name": "Bob", "age": 25, "gender": "female"}

#딕셔너리에 새로운 키와 값을 추가
#대괄호 표기법을 사용하여 키와 값을 추가하는 방법:
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

#update() 메서드를 사용하여 여러 개의 키와 값을 추가하는 방법:
my_dict = {'a': 1, 'b': 2}
my_dict.update({'c': 3, 'd': 4})
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#딕셔너리에서 특정 키와 값 쌍을 제거
fruits = {'apple': 2, 'banana': 3, 'orange': 1, 'grape': 4}
del fruits['orange']
print(fruits)  # {'apple': 2, 'banana': 3, 'grape': 4}

#Dictionary 관련 함수
# 딕셔너리 생성
fruits = {'apple': 3, 'banana': 2, 'orange': 1}

# keys 함수를 사용하여 딕셔너리의 키를 리스트로 변환
keys_list = list(fruits.keys())
print(keys_list)  # ['apple', 'banana', 'orange']

# values 함수를 사용하여 딕셔너리의 값을 리스트로 변환
values_list = list(fruits.values())
print(values_list)  # [3, 2, 1]

# items 함수를 사용하여 딕셔너리의 (키, 값) 쌍을 리스트로 변환
items_list = list(fruits.items())
print(items_list)  # [('apple', 3), ('banana', 2), ('orange', 1)]

# 딕셔너리 생성
fruits = {'apple': 3, 'banana': 2, 'orange': 1}

# get 함수를 사용하여 딕셔너리에서 특정 키에 해당하는 값을 가져옴
print(fruits.get('apple'))  # 3
print(fruits.get('grape'))  # None

# setdefault 함수를 사용하여 딕셔너리에 새로운 (키, 값) 쌍 추가
fruits.setdefault('grape', 5)
print(fruits)  # {'apple': 3, 'banana': 2, 'orange': 1, 'grape': 5}

# pop 함수를 사용하여 딕셔너리에서 특정 키의 (키, 값) 쌍 제거하고 값을 반환
grape_count = fruits.pop('grape')
print(grape_count)  # 5
print(fruits)  # {'apple': 3, 'banana': 2, 'orange': 1}

# update 함수를 사용하여 딕셔너리에 다른 딕셔너리의 (키, 값) 쌍 추가 또는 업데이트
new_fruits = {'pear': 2, 'apple': 5}
fruits.update(new_fruits)
print(fruits)  # {'apple': 5, 'banana': 2, 'orange': 1, 'pear': 2}
