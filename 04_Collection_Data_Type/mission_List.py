#3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오 
fd = ['수현', '원준', '예둥']
fd.insert(0,'지은')
fd.insert(2,'수연')
fd.append('소윤')
print(fd)

#리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.
lis = [1, 2, 3]
#두 번째 요소를 17로 수정
lis[1] = 17
#리스트에 4, 5, 6을 추가
lis += [4, 5, 6]
#첫 번째 요소 제거
del lis[0]
#리스트를 요소 순서대로 배열하기
lis.sort()
#인덱스 3에 25넣기
lis.insert(3,25)
print(lis)

#for 루프를 이용하여 다음과 같은 리스트를 생성하라.
lis = []
#0~49까지의 수로 구성되는 리스트
for l in range(0,50):
    lis.append(l)
    print("요소 추가:",lis)
#1~50까지 수의 제곱으로 구성되는 리스트
lis = [k**2 for k in range(1,51)]
print('제곱수: ', lis)

#크기가 같은 두 개의 리스트 L, M을 생성하고 두 리스트의 각 요소 합으로 구성되는 새로운 리스트를 생성하라. 예를 들어 L=[1,2,3]이고 M=[4,5,6]이면 [5,7,9]인 리스트 생성
L = [1, 2, 3]
M = [4, 5, 6]
re = []
for i in range(len(L)):
    re.append(L[i] + M[i])
print(re)

#사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열을 생성하라. 예를 들어 2, 5, 11, 33, 55를 입력하면 '2+5+11+33+55'를 생성하라.
sen = input("숫자를 입력하시오!").split()
res = "+".join(sen)
print(res)

