#3의 배수와 5의 배수 합 구하기
num = int(input("숫자를 입력하라"))
sum=0
for i in range(1, num+1):
    if(i % 3 == 0 or i %  5 == 0):
        sum += i
    print("3의 배수와 5의 배수의 합은 ",sum,"입니다")

#최댓값과 최솟값 찾기
max_value = 0
min_value = 100
for i in range(5):
    num = int(input("숫자 5개를 입력하라"))
    if(num == 0) :
        break
    if(num > max_value):
        max_value = num
    if(num < min_value):
        min_value = num
print("가장 큰 값은 " ,max_value,"가장 작은 값은",min_value)

#숫자의 합이 100보다 작을 때까지 입력받기
sum = 0
while(sum<100) :
    num = int(input("숫자를 입력하라"))
    sum += num
print("입력한 값들의 합: ", sum)

#피보나치 수열의 n번째 항을 출력
num = int(input("몇 번째 항을 출력할까나?"))
if(num ==1 or num == 2):
    result = 1
else:
    a, b = 1, 1
    i = 3
    while(i <= num):
        result = a + b
        a = b
        b = result
        i +=1
print("피보나치 수열의", num,"번째 합은",result)