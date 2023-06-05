#중괄호 {}를 사용하여 생성하기
my_set = {1, 2, 3, 3, 4, 5, 5}
print(my_set) # {1, 2, 3, 4, 5}

#set() 함수를 사용하여 생성하기
my_set = set([1, 2, 3, 3, 4, 5, 5])
print(my_set) # {1, 2, 3, 4, 5}

#빈 set 생성 후 add() 메소드로 요소 추가하기
my_set = set() #빈 set 만들기
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(3)
my_set.add(4)
my_set.add(5)
print(my_set) # {1, 2, 3, 4, 5}

# set 생성
my_set = {1, 2, 3}

# 개수 확인
print(len(my_set))  # 출력: 3

# 요소 추가
my_set.add(4)
print(my_set)  # 출력: {1, 2, 3, 4}

# 여러 요소 추가
my_set.update([5, 6, 7])
print(my_set)  # 출력: {1, 2, 3, 4, 5, 6, 7}

# 요소 제거 (remove)
my_set.remove(3)
print(my_set)  # 출력: {1, 2, 4, 5, 6, 7}

# 요소 제거 (discard)
my_set.discard(10)  # 요소가 없어도 오류 발생하지 않음
print(my_set)  # 출력: {1, 2, 4, 5, 6, 7}

#add
my_set = {1, 2, 3}
my_set.add(4) # {1, 2, 3, 4}
my_set.add(2) # {1, 2, 3, 4}

#update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)   #{1, 2, 3, 4, 5}
#-----------------------------------------------------
my_list = [5, 6, 7]
my_set = {1, 2, 3}
my_set.update(my_list)   #{1, 2, 3, 5, 6, 7}

#remove
s = {1, 2, 3}
s.remove(2)  # s에서 2를 제거합니다.

if 2 in s:
    s.remove(2)
else:
    print("set에 2가 없습니다.")

#discard
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # 출력: {"apple", "cherry"}

fruits.discard("durian")
print(fruits)  # 출력: {"apple", "cherry"}

#집합 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 합집합
print(set1.union(set2))  # {1, 2, 3, 4, 5}
print(set1 | set2)       # {1, 2, 3, 4, 5}

# 교집합
print(set1.intersection(set2))  # {3}
print(set1 & set2)              # {3}

# 차집합
print(set1.difference(set2))  # {1, 2}
print(set1 - set2)            # {1, 2}

# 대칭차집합
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}
print(set1 ^ set2)                      # {1, 2, 4, 5}

#비교연산
# == 연산자 예시
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {4, 5, 6}
print(set1 == set2) # True
print(set1 == set3) # False

# >, >= 연산자 예시
set4 = {1, 2, 3, 4}
set5 = {1, 2, 3}
print(set4 > set5)  # True
print(set4 >= set5) # True
print(set5 > set4)  # False
print(set5 >= set4) # False

# <, <= 연산자 예시
set6 = {1, 2, 3}
set7 = {1, 2, 3, 4}
print(set6 < set7)  # True
print(set6 <= set7) # True
print(set7 < set6)  # False
print(set7 <= set6) # False

# != 연산자 예시
set8 = {1, 2, 3}
set9 = {3, 2, 1}
set10 = {1, 2, 3, 4}
print(set8 != set9)  # False
print(set8 != set10) # True

#1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램
import random

pick = set()

while (len(pick) < 6):
    n = random.randint(1,45)
    pick.add(n)
print(pick)