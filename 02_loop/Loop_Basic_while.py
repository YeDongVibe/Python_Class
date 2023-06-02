#1부터 10까지 수 출력
i = 1
while i <= 10:
    print(i)
    i += 1

#입력받은 숫자 합(0이면 종료)
sum = 0
while True:
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        break
    sum += num
print("입력한 값들의 합: ", sum)

#입력받은 숫자 중 가장 큰 값 출력
max_value = 0
while(True) :
    num = int(input("숫자를 입력하세요. : "))
    if (num == 0) :
        break
    if (num > max_value) :
        max_value = num
print("가장 큰 값은 " ,max_value)