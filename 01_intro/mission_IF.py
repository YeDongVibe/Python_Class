#인치 변환
# num1 = int(input("몇 cm인가?"))
# if(num1 <0) :
#     print("잘못 입력했다. 똑바로 입력하3")
# else :
#     len = num1/2.54
#     print(f"그대가 입력한 {num1}cm는 {len:.2f}인치이다.")

#학점 졸업 판단
# num1 = int(input("몇 학점 이수했니?"))
# if(num1 < 40):
#     print("1학년이네?")
# elif(40<num1<80) :
#     print("2학년이네?")
# else :
#     print("응. 졸업 준비 잘하고^^")

#최종시간 출력
num1 = int(input("몇시고?"))
dn = input("am이여? pm이여?")
num2 = int(input("얼마나 시간이 지났니?"))

if(dn == 'am') :
    if(num1 + num2 < 12) :
        time = num1 + num2
    else : 
        time = num1 + num2 -12
else:
    if(num1 + num2 < 12) :
        time = num1 + num2
    else :
        time = num1 + num2 -12

print(f"지금은 {time}시네")