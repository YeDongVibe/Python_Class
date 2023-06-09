#data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6} 이 주어질 때 try-except문을 이용하여 다음과 같이 동작하는 프로그램을 작성하라.
# 사용자로부터 문자열을 입력 받는다
# 문자열이 data의 key와 같으면 value를 출력하고 다시 문자열을 입력 받는다
# 문자열 에 해당하는 key가 없으면 "항목이 없습니다"라는 메시지를 출력하고 종료한다.

# 위 문제를 try-except를 이용하지 않고 프로그램할 수 있는가? 차이점은 무엇인가?
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}
while (True):
    try:
        st = input("요일을 입력하라")
        val = data.get(st)
        print(val)
        break
    except:
        print("except : 항목이 없습니다")
        break
    
