#if~else문
# num = int(input("숫자를 입력하세요: "))

# if num % 2 == 0:
#     print(f"{num}은(는) 짝수입니다.")
# else:
#     print(f"{num}은(는) 홀수입니다.")

#if~elif~else문
# num = int(input("숫자를 입력하세요: "))

# if num > 0:
#     print("양수입니다")
# elif num < 0:
#     print("음수입니다")
# else:
#     print("0입니다")

#한문장의 if~elif~else문
# score = int(input("성적을 입력하세요: "))
# grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
# print("학점 : " + grade)

#입력 문자열 출력
# string = input("문자열을 입력하세요: ")
# length = len(string) if string else 0
# print("문자열의 길이는", length, "입니다.")

#성적 출력 계산기(한줄 loop문)
# num1 = int(input("국어 점수 몇점이고? : "))
# num2 = int(input("영어 점수 몇점이고? : "))
# num3 = int(input("수학 점수 몇점이고? : "))

# avg = (num1 + num2 + num3)/3

# grade = 'A' if avg >= 90 else('B' if avg >= 80 else('C' if avg >= 70 else ('D' if avg >= 60 else 'F')))
# print(f"그대의 평균 점수는 {avg:.2f}이므로, 학점은 {grade} 이니라.")

#성적 출력 계산기(여러 줄 loop)
# num1 = int(input("국어 점수 몇점이고? : "))
# num2 = int(input("영어 점수 몇점이고? : "))
# num3 = int(input("수학 점수 몇점이고? : "))

# avg = (num1*0.4 + num2*0.4 + num3*0.2)

# if (avg >=90):
#     grade = 'A'
# elif (avg >=80):
#     grade = 'B'
# elif (avg >=70):
#     grade = 'C'
# elif (avg >=60):
#     grade = 'D'
# else :
#     grade = 'F'

# print(f"그대의 평균 점수는 {avg:.2f}이므로, 학점은 {grade} 이니라.")