#문자열 합치기
s1 = "Hello"
s2 = "world"
s3 = s1 + s2

#문자열 반복
s4 = "Ha"
s5 = s4 * 3
print(s5) 

#문자열 길이 구하기
s6 = "Python is awesome"
print(len(s6))

#문자열 인덱싱
s = "Python is a fun programming language!"
print(s[7]) 
print(s[11]) 
print(s[-12])

#문자열 인덱싱
s = "ABCDEFG"
print(s[1:4]) 
print(s[:3])  
print(s[3:])  

#문자열 인덱싱
s = "Hello, World!"
print(s[0])  
print(s[1])   
print(s[-1])  

#첫번째, 마지막 문자 출력
string = input("문자열을 입력하세요: ")

first = string[0]
last = string[-1]

print("첫 번째 문자는 %s입니다." % first)
print("마지막 문자는 %s입니다." % last)

#문자열에서 홀수 번째 문자 추출
string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]

print(result)  # 출력값: "acegi"

#Hello World에서 World 추출 하기
string = "hello world"
substring = string[6:]
print(substring)

#Hello World에서 hello 추출 하기
string = "hello world"
substring = string[:5]
print(substring)

#hello world에서 hlowrd 부분 문자열을 추출
string = "hello world"
substring = string[::2]
print(substring)  # "hlowrd"

#문자열 뒤집기
s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # "!dlrow ,olleH"

#문자열 수정
s = "Hello"
s = "h" + s[1:]
print(s)  # "hello"

# 문자열 구성 파악 메소드 예시
print("hello123".isalnum())  # True
print("123".isalpha())  # False
print("123".isdecimal())  # True
print("123".isdigit())  # True
print("hello".isidentifier())  # True
print("hello".islower())  # True
print("123".isnumeric())  # True
print("Hello, World!".isprintable())  # True
print("   ".isspace())  # True
print("\t".isspace())  # True
print("Hello, World!".istitle())  # True
print("HELLO".isupper())  # True

# 문자열 대소문자 변환 함수 예시
print("hello, world!".upper())  # "HELLO, WORLD!"
print("HeLLo, wOrLd!".lower())  # "hello, world!"
print("hello, world!".capitalize())  # "Hello, world!"
print("hello, world!".title())  # "Hello, World!"
print("Hello, World!".swapcase())  # "hELLO, wORLD!" 소문자는 대문자로, 대문자는 소문자로 바꿔줌

# 문자열 찾기 함수 예시
s = "hello, world!"

print(s.find("o"))  # 4
print(s.rfind("o"))  # 8
print(s.index("o"))  # 4
print(s.rindex("o"))  # 8
print(s.count("o"))  # 2

# 문자열 공백 삭제 및 변경 함수 예시
s = "  hello,   world!  "

print(s.strip())  # "hello,   world!"
print(s.lstrip())  # "hello,   world!  "
print(s.rstrip())  # "  hello,   world!"
print(s.replace("o", "0"))  # "  hell0,   w0rld!  "
print(s.replace("o", "0", 1))  # "  hell0,   world!  "

# 문자열 분리, 결합 함수 예시
s = "apple,banana,grape"

print("apple\nbanana\rgrape".splitlines())  # ["apple", "banana", "grape"]
print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"

# 문자열 정렬, 채우기 함수 예시
s = "hello"

print(s.center(10))  # "  hello   "
print(s.center(10, "-"))  # "--hello---"
print(s.ljust(10))  # "hello     "
print(s.ljust(10, "*"))  # "hello*****"
print(s.rjust(10))  # "     hello"
print(s.rjust(10, "+"))  # "+++++hello"
print("123".zfill(5))  # "00123"
