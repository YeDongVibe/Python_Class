#예외의 종류와 각각에 대한 설명

# ValueError: 잘못된 값이 사용될 때 발생
num = int("not_a_number")

#-----------------------------------------------------------------------------------------------------------------
# TypeError: 잘못된 타입의 객체가 사용될 때 발생
result = "string" + 1

#-----------------------------------------------------------------------------------------------------------------
# IndexError: 인덱스 범위를 벗어난 경우 발생
numbers = [1, 2, 3]
out_of_range = numbers[3]

#-----------------------------------------------------------------------------------------------------------------
# KeyError: 사전에서 존재하지 않는 키를 참조할 때 발생
my_dict = {"a": 1, "b": 2}
value = my_dict["c"]

#-----------------------------------------------------------------------------------------------------------------
# FileNotFoundError: 존재하지 않는 파일을 열려고 시도할 때 발생
with open("non_existing_file.txt", "r") as file:
    content = file.read()

#================================================================================================================
#try~except 문
#ValueError 처리 예시
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.") #에러 메시지 표시

#-----------------------------------------------------------------------------------------------------------------

#FileNotFoundError 처리 예시
try:
    with open("non_existing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist. Please check the file path.") #에러 메시지 표시

#-----------------------------------------------------------------------------------------------------------------

#한 개의 except블록으로 여러 예외 처리
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.") #에러 메시지 표시

#-----------------------------------------------------------------------------------------------------------------

#각각의 예외를 별도의 except블록으로 예외 처리
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.") #에러 메시지 표시
except ZeroDivisionError:
    print("Cannot divide by zero!") #에러 메시지 표시

#================================================================================================================
#as 키워드
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except Exception as e:
    print(f"An error occurred: {e}") #에러 메시지 표시

#-----------------------------------------------------------------------------------------------------------------
try:
    # 예외가 발생할 수 있는 코드를 실행합니다.
    file = open("non_existent_file.txt", "r")
    result = 5 / 0
    int("not_a_number")
except FileNotFoundError as error:
    print(f"An error occurred: {error}") #에러 메시지 표시
except ZeroDivisionError as error:
    print(f"An error occurred: {error}") #에러 메시지 표시
except ValueError as error:
    print(f"An error occurred: {error}") #에러 메시지 표시

#-----------------------------------------------------------------------------------------------------------------
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except Exception as e:
    print(f"An error occurred: {e}")

#================================================================================================================
#try-except-else
# try:
#     # 예외가 발생할 수 있는 코드
# except [예외 타입]:
#     # 예외가 발생했을 때 실행할 코드
# else:
#     # 예외가 발생하지 않았을 때 실행할 코드

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"You entered the number {number}.")

#-----------------------------------------------------------------------------------------------------------------
#파일 읽기 예시
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
    file.close()

#================================================================================================================
#try-except-finally
# try:
#     # 예외가 발생할 수 있는 코드
# except ExceptionType1:
#     # 예외 타입 1이 발생한 경우 실행할 코드
# except ExceptionType2:
#     # 예외 타입 2가 발생한 경우 실행할 코드
# # ... 필요한 만큼의 except 블록을 추가
# finally:
#     # 예외 발생 여부와 상관없이 항상 실행할 코드

#파일 읽기
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File has been closed.")
