#1~n까지의 합을 계산하는 함수
def cal_(a):
    total = 0
    for i in range(1,a+1):
        total += i
    return total
print('1부터 n까지의 합')
print(cal_(50))

#반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성하라. 이들 함수를 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 소수점 아래 첫 자리까지 구하라.
# def cir_area(r):


#den(n) 함수를 이용하여 약수를 구하여 반환하는 프로그램을 작성
#12 → [1, 2, 3, 4, 6, 12]


#두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 
def box_(c, d):
    for i in range(c):
        for j in range(d):
            print("*", end="")
        print()
print('박스별')
print(box_(5,4))

#두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
def str_comp(str1, str2):
    length = min(len(str1), len(str2))
    for i in range(length):
        if (str1[i] != str2[i]):
            return i
    return -1
print('문자열 같냐 다르냐')
print(str_comp('abc', 'abcd'))

#문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
def find_char(e,f):
    res = []
    for i in range(len(e)):
        if e[i] == f:
            res.append(i)
    return res
print('문자위치 리스트 반환')
print(find_char('aabcbcdb', 'b'))

#재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
def cal_(g):
    if (g ==1):
        return 1
    else:
        return g + cal_(g-1)
print('1부터 100까지의 합')
print(cal_(100))


#enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서 'a' 문자의 위치를 모두 찾아 출력하는 프로그램을 작성하라. 'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.


#두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라. 딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, '2'를 입력하면 sub(), '3'을 입력하면 mul(), '4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는 프로그램을 작성하라.


#다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성 예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때 {'led':'on', 'motor':'off', 'switch':off'} 반환.Hint: dict([['a','b'], ['c', 'd']])  {'a': 'b', 'c': 'd'}
