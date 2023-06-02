#주사위 게임
import random

rnum = random.randint(1,6)
rnum2 = random.randint(1,6)
if (rnum + rnum2 == 7):
    print(rnum,',',rnum2,"을 뽑았으므로 넌 Winner")
else :
    print(rnum,',',rnum2,"을 뽑았으므로 넌 loser")

#계산기 프로그램
while(True):
    num1 = int(input("첫 번째 수를 입력하라"))
    num2 = int(input("두 번째 수를 입력하라"))
    op = input("연산자를 입력하라(+, -, *, /) / 종료하고싶으면 exit 입력 ㄱ")
    if(op == 'exit'):
        break
    elif(op == '+'):
        res = num1 + num2
    elif(op == '-'):
        res = num1 - num2
    elif(op == '*'):
        res = num1 * num2
    elif(op == '/'):
        res = num1 / num2
    print("결과값은",res,"입니다.")

#숫자 맞추기 게임
import random

for i in range(1,6):
    secret_number = random.randint(1, 100)
    num1 = int(input("수를 입력하라"))
    if(num1 == secret_number):
        print(i,"번만에 맞추었습니다!")
    else:
        print("못맞췄지렁~~")

#동전 야바위
import random

res = 50
while(True):
    coin = random.randint(1,2)
    num1 = int(input("수를 입력하라"))
    if(coin == num1):
        res +=9
        print("맞췄네^^")
    elif(coin != num1):
        res -=10
        print("틀렸대요~")
    elif(res == 0):
        print("응 다 날렸대^^")
        break
    elif(res == 100):
        print("잘...하네?")
        break

#공약수
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

result = gcd(num1, num2)
print("두 수의 최대 공약수는", result, "입니다.")

#약수 출력
num = int(input("수를 입력하세요: "))
for i in range(1,num+1):
    if(num % i == 0):
        print(num,"의 약수는 ",i,"여")

#성적 출력
while(True):
    num = int(input("첫 번째 수를 입력하세요: "))
    if(num <0 ):
        break
    elif(num >= 90):
        res = 'A'
    elif(num >= 80):
        res = 'B'
    elif(num >= 60):
        res = 'C'
    elif(num >= 40):
        res = 'D'
    else:
        res = 'F'
    print("그대의 성적은",res,"입니다.")

#소수 출력
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("자연수 n을 입력하세요: "))

print("2부터", n, "까지의 소수는:")
for i in range(2, n + 1):
    if is_prime(i):
        print(i)
