# 정규표현식 : 정규표현식(Regular Expression)은 문자열을 처리하는 패턴을 정의하는데 사용되는 형식 언어. 정규표현식은 문자열의 검색(search)과 치환(replace) 작업에 사용됩니다.

# 정규표현식의 구성 요소
# 정규표현식은 메타 문자(meta character)와 리터럴(literal)로 이루어져 있음. 메타 문자는 특별한 의미를 가지며, 리터럴은 문자 그대로를 의미.

# 정규표현식의 메타 문자
# . (마침표) : 임의의 문자 한 개를 의미.
# ^ (캐럿) : 문자열의 시작을 의미.
# $ (달러) : 문자열의 끝을 의미.
# * (별표) : 0개 이상의 문자를 의미.
# + (더하기) : 1개 이상의 문자를 의미.
# ? (물음표) : 0개 또는 1개의 문자를 의미.
# [] : 대괄호 안에 나열된 문자 중 하나와 매칭.
#   [a-z] : 알파벳 소문자 중 하나와 매칭.
#   [A-Z] : 알파벳 대문자 중 하나와 매칭.
#   [0-9] : 숫자 중 하나와 매칭.
# | : OR 연산자 역할을 하며, 왼쪽 또는 오른쪽 패턴 중 하나와 매칭.
# () : 그룹핑을 위해 사용되며, 매칭 결과에 대한 그룹을 생성.
# {} : 중괄호 안에 숫자가 들어가며, 앞의 문자나 패턴이 해당 숫자만큼 나타나는 패턴과 매칭.
# () : 그룹핑을 위해 사용되며, 매칭 결과에 대한 그룹을 생성.
# \ : 이스케이프 문자로 사용되며, 메타문자를 문자 그대로 매칭시키기 위해 사용.
# \d : 숫자와 매칭.
# \D : 숫자가 아닌 문자와 매칭.
# \w : 숫자와 알파벳(대소문자), 언더스코어(_)와 매칭.
# \W : 숫자와 알파벳(대소문자), 언더스코어(_)가 아닌 문자와 매칭.
# \s : 공백 문자와 매칭.
# \S : 공백 문자가 아닌 문자와 매칭.
# \b : 단어(word) 경계를 나타내는 메타문자

# 정규표현식의 리터럴 : 정규표현식의 리터럴은 문자 그대로를 의미. 예를 들어, "hello"는 정규표현식에서 "hello"라는 문자 그대로를 의미.

#================================================================================================================
# 문자열 매칭 : 정규표현식을 사용하여 문자열 내에서 특정한 패턴을 검색하는 과정
# r을 붙인 패턴 문자열은 Raw String(원시 문자열)로 해석되어 백슬래시를 이스케이프 문자가 아니라 일반 문자로 처리.

# re.match() 함수 : 문자열의 시작에서 패턴을 찾아서 반환. 예를 들어, re.match(r"abc", "abcdef")는 "abc"와 매칭.
import re

# 문자열의 시작부터 정규표현식과 매칭되는 패턴 찾기
pattern = r"python"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)
match3 = re.match(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")

#-----------------------------------------------------------------------------------------------------------------
# re.search() 함수 : 문자열 내에서 패턴을 검색하여 반환. 예를 들어, re.search(r"abc", "defabc")는 "abc"와 매칭.
import re

# 문자열 전체에서 정규표현식과 매칭되는 패턴 찾기
pattern = r"python"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)
match3 = re.search(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")

#================================================================================================================
#문자열 추출 : 문자열 추출은 정규표현식을 사용하여 문자열 내에서 특정한 패턴을 검색하고 추출하는 과정.
#re.findall() : 문자열 내에서 패턴과 매칭된 모든 부분을 리스트로 반환. 
#예를 들어, re.findall("a", "abcdaaa")는 ['a', 'a', 'a', 'a']와 같은 리스트를 반환합니다.
import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴 찾기
pattern = r"\d+"
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

matches1 = re.findall(pattern, string1)
matches2 = re.findall(pattern, string2)
matches3 = re.findall(pattern, string3)

print(matches1)  # ['2', '3']
print(matches2)  # ['-1', '5']
print(matches3)  # ['12345678']

#================================================================================================================
#그룹핑 : 그룹핑은소괄호(())로 표현하며, 그룹핑된 문자열은 ()안에 위치. 그룹핑된 문자열은 해당 그룹핑의 순서대로 1, 2, 3...과 같은 그룹핑 인덱스를 부여. 
#전화번호에서 지역번호와 나머지 번호를 각각 추출
import re

phone_number = "010-1234-5678"
pattern = r"(\d{2,3})-(\d{3,4})-(\d{4})"
result = re.match(pattern, phone_number)

area_code = result.group(1)
phone_number_without_area_code = result.group(2) + "-" + result.group(3)

print(area_code)  # 010
print(phone_number_without_area_code)  # 1234-5678

#-----------------------------------------------------------------------------------------------------------------
#날짜 표기법 변환
import re

date = "2022-03-18"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
result = re.sub(pattern, r"\2/\3/\1", date)

print(result)  # "03/18/2022"

#-----------------------------------------------------------------------------------------------------------------
#이름 순서 바꾸기
import re

string = "Kim, Yuna"
pattern = r"(\w+),\s*(\w+)"
result = re.sub(pattern, r"\2 \1", string)
print(result)  # "Yuna Kim"

#================================================================================================================
#정규표현식 패턴 옵션
#정규표현식에서 사용되는 패턴 옵션은 대소문자 무시, 다중행 모드 등이 있음.
#re.IGNORECASE : re.IGNORECASE 옵션은 대소문자를 무시. 예를 들어, re.findall(r"a", "AbCdAaA", re.IGNORECASE)는 ['A', 'a', 'A', 'a', 'A']와 같은 리스트를 반환.
string = "Python is an interpreted language"

import re

pattern = 'python'
result = re.findall(pattern, string)
print(result)  # []

result = re.findall(pattern, string, re.IGNORECASE)
print(result)  # ['Python']


#re.MULTILINE : re.MULTILINE 옵션은 다중행 모드를 사용. 예를 들어, "abc\ndef\nghi"라는 문자열에서 r"^g"를 검색할 때, re.MULTILINE 옵션이 적용되면 "g"와 매칭.
string = """Python is an interpreted language
It is dynamically typed
And it is easy to learn"""

import re

pattern = '^Python|typed$'
result = re.findall(pattern, string, re.MULTILINE)
print(result)  # ['Python', 'typed']

#================================================================================================================
#정규표현식 활용 예제
#이메일 주소 추출
import re

def extract_email(string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, string)
    return emails


string = "John's email is john.doe123@example.com. Jane can be reached at jane@example.co.uk."

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']

#-----------------------------------------------------------------------------------------------------------------
#메일 주소의 유효성을 검증하는 예제
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = 'example@example.com'
email2 = 'example@example.co.kr'
email3 = 'example.example.com'
email4 = 'example@example.'
email5 = 'example@example'

print(is_valid_email(email1))  # True
print(is_valid_email(email2))  # True
print(is_valid_email(email3))  # False
print(is_valid_email(email4))  # False
print(is_valid_email(email5))  # False

#-----------------------------------------------------------------------------------------------------------------
#전화번호 유효성 검증하는 예제
import re

def is_valid_phone_number(phone_number):
    pattern = r'^\d{3}-\d{3,4}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

phone_number1 = '010-1234-5678'
phone_number2 = '02-123-4567'
phone_number3 = '123-4567'

print(is_valid_phone_number(phone_number1))  # True
print(is_valid_phone_number(phone_number2))  # True
print(is_valid_phone_number(phone_number3))  # False

#-----------------------------------------------------------------------------------------------------------------
#로그 데이터에서 IP 주소를 추출하는 예시
import re

log_data = [
    '192.168.0.1 - - [21/Feb/2022:10:12:01 +0900] "GET /index.html HTTP/1.1" 200 2326',
    '192.168.0.2 - - [21/Feb/2022:10:12:02 +0900] "GET /images/banner.jpg HTTP/1.1" 200 6571',
    '192.168.0.3 - - [21/Feb/2022:10:12:03 +0900] "POST /login.php HTTP/1.1" 302 -',
    '192.168.0.4 - - [21/Feb/2022:10:12:04 +0900] "GET /favicon.ico HTTP/1.1" 404 209'
]

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

for log in log_data:
    ip = re.findall(ip_pattern, log)
    print(ip)
