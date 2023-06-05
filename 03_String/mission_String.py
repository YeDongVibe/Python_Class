#문자열의 문자수를 출력하라
# sen = input("문장 입력하시오!")
# print(len(sen))

#문자열을 10번 반복한 문자열을 출력하라
# sen = input("문장 입력하시오!")
# res = sen * 5
# print(res)

#문자열의 첫 번째 문자를 출력하라
# sen = input("문장 입력하시오!")
# print(sen[0])

#문자열에서 처음 3문자를 출력하라
# sen = input("문장 입력하시오!")
# print(sen[0:3])

#문자열에서 마지막 3문자를 출력하라
# sen = input("문장 입력하시오!")
# print(sen[-3:])

#문자열의 문자를 거꾸로 출력하라
# sen = input("문장 입력하시오!")
# res = sen[::-1]
# print(res)

#문자열에 7번째 문자가 있으면 출력하고 없으면 '문자가 없습니다'라는 메시지를 출력하라
# sen = input("문장 입력하시오!")
# if(len(sen) >= 7):
#     print(sen[6])
# else:
#     print("문자가 없슴돠")

#문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라
#sen = input("문장 입력하시오!")


#문자를 모두 대문자로 변경하여 출력하라
#sen = input("문장 입력하시오!")

#문자를 모두 소문자로 변경하여 출력하라
#sen = input("문장 입력하시오!")

#문자열에서 'a'를 'e'로 대체하여 출력하라
#sen = input("문장 입력하시오!")

#문자 'a'가 들어가는 단어를 키보드에서 입력 받아 첫 번째 줄에는 'a'까지의 문자열을 출력하고 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.
sen = input("문장 입력하시오!")
s_find = sen.find("a")
if(s_find != -1):
    print(sen[:s_find+1])
    print(sen[s_find+1:])
else:
    print("없다링없다링")

#1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라

for num in range(1,1001):
    sum = 0
    for tsum in str(num):
        sum += int(tsum)
print(sum)

    