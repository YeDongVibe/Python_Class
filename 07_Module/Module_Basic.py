#모듈 불러오기
#import <module-name>

#dir() 함수 : 모듈이나 클래스에 포함된 변수, 메소드, 클래스 등의 속성들을 확인할 수 있습니다.
import random

print('='*70)
print(dir(random)) # random 모듈 내에 포함된 변수, 함수, 클래스 등을 나열합니다.
print('-'*70)
print(help(random.choice)) # random 모듈 내에 포함된 choice 함수의 도움말을 출력합니다.
print('-'*70)

#from import : from import는 모듈에서 특정 변수, 함수, 클래스 등을 가져올 때 사용됩니다
from math import sqrt, pi

print('='*70)
print(sqrt(4))  # 출력 결과: 2.0 # from ~~ import ~~ 이렇게 쓰면 함수이름을 그대로 가져와 사용 가능
print('-'*70)
print(pi)  # 출력 결과: 3.141592653589793
print('-'*70)

#from import * : *를 사용하여 모든 변수, 함수, 클래스 등을 가져오는 것은 권장되지 않습니다. 왜냐하면, 모듈에서 모든 것을 가져오면 현재 스코프에서 이름 충돌이 일어날 수 있기 때문입니다. 또한, 모듈에서 사용하지 않는 함수나 클래스도 불필요하게 가져오기 때문에 메모리 낭비가 발생할 수 있습니다.
from math import *

print('='*70)
print(sqrt(9))  # 출력 결과: 3.0
print('-'*70)
print(pi)  # 출력 결과: 3.141592653589793
print('-'*70)
print(sin(pi/2))  # 출력 결과: 1.0
print('-'*70)

#import as : 모듈을 불러올 때 해당 모듈에 별칭(alias)을 지어주는 방법입니다.
import math as m

print('='*70)
print(m.sqrt(4))  # 2.0
print('-'*70)
print(m.pi)  # 3.141592653589793
print('-'*70)

#sys.path : 현재 파이썬 인터프리터가 모듈을 검색할 경로들을 담고 있는 리스트
import os, sys

print('='*70)
print(os.getcwd()) #현재 디렉토리 표시
print('-'*70)
print(sys.path) #환경변수에 지정된 디렉토리
print('-'*70)

#================================================================================================================
#사용자 정의 모듈
#my_module.py : Python 파일을 만들어서 제작(사용자 모듈 제작)
# def greet(name):
#     print(f"Hello, {name}!")

#main.py : 사용자가 만든 모듈을 import하여 사용
# import my_module

# my_module.greet("Alice")  # "Hello, Alice!" 출력

#-----------------------------------------------------------------------------------------------------------------
#if __name__ == '__main__' : 메인 파일에서는 사용 가능하지만 다른 모듈에서 import할 때는 사용 불가
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    print(add(3, 5))
    print(subtract(10, 7))
