# Deposit 클래스를 생성하라. 이 클래스는 세 개의 인스턴스 변수 initial과 interest, n을 갖는다. initial은 원금을 의미하고 interest는 년 이자율을 나타낸다. 초기화 함수에서 세 개의 인스턴스 변수를 전달 받은 값으로 설정해야 한다. 클래스 메소드 profit()은 n년 후 원리금을 반환한다. n년 후 원리금은 initial * (1 + interest)n이다. Deposit 클래스를 이용하여 100만원을 이율 3.5%로 7년간 저축했을 때 원리금을 구하는 프로그램을 작성하라. 단 원리금은 정수로 표시되어야 한다.
class Deposit:
    def __init__(self, initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n

    def reset(self):
        return int(self.initial * (1 + self.interest)*(self.n))
    
deposit1 = Deposit(1000000, 0.035, 7)

print('원금리는 ',deposit1.reset())
print('-'*50)

#예제의 Teacher 클래스에서 People 클래스의 __init__()를 호출하지 않고 부모 클래스의 age, name 인스턴스 변수를 이용할 수 있는가? 이용할 수 없다면 그 이유는? 이용할 수 있게 하려면 프로그램을 어떻게 수정해야 하는가?
class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))
        
    #get.set을 추가해야지 동작 가능
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if (age > 0):
            self.__age = age
        else:
            print('잘못된 나이입니다.')

class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

t = Teacher(36, "Kim", 'High School')
t.introMe()
t.showSchool()
print('-'*50)

t.set_name("Lee")
t.set_age(47)
t.introMe()
print('-'*50)

#다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라. Employee 클래스에 employeeID 인스턴스 변수를 추가하고 getID() 메소드를 정의하라. getID() 메소드는 employeeID를 반환하는 메소드이다. Employee 클래스를 이용하여 Employee("동양", 65, 2019)로 생성된 객체의 이름, 나이, ID를 출력하라.
class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        return self.name # Python에서는 return값이 없으면 none을 return함

    def getAge(self): 
        return self.age

class Employee(Person):
    def __init__(self, name, age , employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID

    def getID(self):
        return self.employeeID
    
emp = Employee("동양", 65, 2019)
print(emp.getName(), emp.getAge(), emp.getID())
print('-'*50)