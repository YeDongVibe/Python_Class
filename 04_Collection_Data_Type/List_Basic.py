# 정수와 실수가 포함된 리스트
mixed_list = [1, 2.5, 3, 4.2, 5]

# 문자열과 불리언 값이 포함된 리스트
string_bool_list = ['hello', True, 'world', False]

# 리스트와 튜플이 포함된 리스트
list_tuple_list = [[1, 2, 3], (4, 5, 6), [7, 8, 9]]

# 리스트와 딕셔너리가 포함된 리스트
list_dict_list = [[1, 2, 3], {'a': 4, 'b': 5, 'c': 6}, [7, 8, 9]]

# 리스트와 집합이 포함된 리스트
list_set_list = [[1, 2, 3], {4, 5, 6}, [7, 8, 9]]

#1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트를 생성
evenNum = [nums for nums in range(1,11) if nums % 2 ==0]
print(evenNum)

#리스트 내 모든 요소에 1을 더하는 예제
original_list = [1, 2, 3, 4, 5]
new_list = [num + 1 for num in original_list]
print(new_list)  # [2, 3, 4, 5, 6]

#리스트 내 문자열의 길이를 구하는 예제
words = ['apple', 'banana', 'cherry', 'durian']
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 6, 6, 6]

#문자열 리스트에서 길이가 5 이상인 문자열만 대문자로 바꾸기
words = ["apple", "banana", "orange", "grape", "watermelon"]
result = [word.upper() for word in words if len(word) >= 5]
print(result)  # ['BANANA', 'ORANGE', 'WATERMELON']

#리스트 내 중첩된 요소들을 단일 리스트로 만드는 예제
original_list = [[1, 2], [3, 4], [5, 6]]
new_list = [num for sublist in original_list for num in sublist]
print(new_list)  # [1, 2, 3, 4, 5, 6]

#주어진 이차원 리스트에서 짝수만 리스트로 생성하기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)  # [2, 4, 6, 8]

#리스트 인덱스 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])  # [1, 2, 3] 출력
print(matrix[1])  # [4, 5, 6] 출력
print(matrix[2])  # [7, 8, 9] 출력
print(matrix[0][1])  # 2 출력
print(matrix[1][2])  # 6 출력

#리스트 슬라이싱
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])   # [2, 3, 4]
print(my_list[:3])    # [1, 2, 3]
print(my_list[2:])    # [3, 4, 5]
print(my_list[::2])   # [1, 3, 5]

#리스트 합치기(+.- 이용)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3) # 출력 결과: [1, 2, 3, 4, 5, 6]

#리스트 합치기(extend) 이용)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
list3 = list1
print(list3) # 출력 결과: [1, 2, 3, 4, 5, 6]

#리스트에 요소 추가
my_list = [1, 2, 3, 4]

my_list.append(5)
print(my_list) # 출력 결과: [1, 2, 3, 4, 5]

my_list.insert(2, 5)
print(my_list) # 출력 결과: [1, 2, 5, 3, 4]

#리스트에 요소 제거
my_list = [1, 2, 3, 4, 5]

my_list[1:4] = []
print(my_list) # 출력 결과: [1, 5]

del my_list[2]
print(my_list) # 출력 결과: [1, 2, 4]

my_list.remove(3)
print(my_list) # 출력 결과: [1, 2, 4]

my_list.pop()
print(my_list) # 출력 결과: [1, 2, 3]

my_list.clear()
print(my_list) # 출력 결과: []

#리스트 정렬
nums = [3, 5, 1, 4, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 3, 4, 5]

reversed_nums = list(reversed(nums)) #reverse는 list로 저장되는 것이 아니기에 list로 변환 해야함.
print(reversed_nums)  # [2, 4, 1, 5, 3]


nums.sort() #무조건 오름차순
print(nums) #[1, 2, 3, 4, 5]

a = [3, 2, 1]
b = sorted(a)
print(a)  # 출력: [3, 2, 1]
print(b)  # 출력: [1, 2, 3]
