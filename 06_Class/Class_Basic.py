#Class : 아이폰 설계도
#instance : 개인이 가지고 있는 아이폰
#instance 변수 : 개인 데이터
#instance 매서드 : 아이폰의 기능(전화, 메시지 등)
#Class 변수 : 앱스토어

#------------------------------------------------------------------------------------------------------------------
# class 클래스이름:
#     # 클래스 멤버 변수
#     클래스변수 = 값
    
#     # 생성자 메서드<__init__()>
#     def __init__(self, 매개변수):
#         # 인스턴스 멤버 변수
#         self.인스턴스변수 = 매개변수
        
#     # 인스턴스 메서드
#     def 메서드이름(self, 매개변수):
#         # 메서드 내용
#------------------------------------------------------------------------------------------------------------------
#생성자
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 인스턴스 생성 시 생성자 메서드 호출
rectangle1 = Rectangle(3, 4)
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4

print(rectangle1.area()) # 인스턴스 메서드 호출 # 출력 결과: 12

#================================================================================================================
#self이용한 인스턴스 변수 접근
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 인스턴스 생성
rectangle1 = Rectangle(3, 4)

print(rectangle1.area()) # 인스턴스 메서드 호출 # 출력 결과: 12

#================================================================================================================
#class를 이용한 인스턴스를 생성하는 예시
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 인스턴스 생성
rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(5, 6)

# 인스턴스 변수에 접근하여 값 출력
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4
print(rectangle2.width) # 출력 결과: 5
print(rectangle2.height) # 출력 결과: 6

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
print(rectangle2.area()) # 출력 결과: 30

#================================================================================================================
#인스턴스 변수를 이용한 예시 <인스턴스 변수는 생성자 메서드(__init__) 내부에서 self.변수이름 형식으로 정의>
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 인스턴스 변수를 이용하여 객체 생성
rectangle1 = Rectangle(3, 4) #인스턴스 변수명을 이용해 생성
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4

# 인스턴스 변수 값 변경
rectangle1.width = 5
print(rectangle1.width) # 출력 결과: 5

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 20

#================================================================================================================
#Class 변수<클래스 변수는 생성자 메서드(__init__) 내부가 아닌 클래스 내부에서 정의>
class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self):
        return self.width * self.height

# 클래스 변수 값을 출력 / 클래스명.변수
print(Rectangle.count) # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
print(Rectangle.count) # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
print(Rectangle.count) # 출력 결과: 2

#================================================================================================================
#인스턴스 매서드 <인스턴스 메서드(Instance Method)는 해당 클래스의 인스턴스(객체)를 통해 호출되는 메서드>
#인스턴스 메서드는 클래스 내부에 정의되며, 첫 번째 인자로 self를 받음

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle1 = Rectangle(3, 4) # 인스턴스 생성

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
print(rectangle1.perimeter()) # 출력 결과: 14

#------------------------------------------------------------------------------------------------------------------

class Bicycle:
    # 생성자 메서드
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    # 인스턴스 메서드
    def speed_up(self, increment):
        self.speed += increment

    def apply_brake(self, decrement):
        self.speed -= decrement

#================================================================================================================
#Class 매서드 <클래스 메서드는 @classmethod 데코레이터를 이용하여 정의하며, 첫 번째 인자로 cls를 받음>
class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    @classmethod
    def print_count(cls):
        print(cls.count)

# 클래스 메서드 호출
Rectangle.print_count() # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
Rectangle.print_count() # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
Rectangle.print_count() # 출력 결과: 2

#------------------------------------------------------------------------------------------------------------------

class Calculator:
    # 클래스 변수
    operator = '+'

    # 클래스 메서드
    @classmethod
    def set_operator(cls, new_operator):
        cls.operator = new_operator

    # 인스턴스 메서드
    def calculate(self, num1, num2):
        if Calculator.operator == '+':
            return num1 + num2
        elif Calculator.operator == '-':
            return num1 - num2
        elif Calculator.operator == '*':
            return num1 * num2
        elif Calculator.operator == '/':
            return num1 / num2


#================================================================================================================
#캡슐화<캡슐화란, 클래스나 모듈 안에 정의된 변수나 함수를 외부에서 직접 접근할 수 없도록 하는 것을 의미>
#인스턴스 변수 이름 앞에 밑줄 두 개(__)를 붙여서 비공개 인스턴스 변수로 만들어 캡슐화를 구현

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # age 인스턴스 변수를 비공개로 설정

p = Person("Alice", 25)
print(p.name)   # Alice
print(p.__age)  # 비공개 인스턴스 변수에 접근 시 에러 발생

#================================================================================================================
#getter/setter 메서드 <직접적으로 인스턴스 변수에 접근할 수 없는 경우, 메서드를 통해 간접적으로 접근하는 방법>
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

#================================================================================================================
#상속 <상속(Inheritance)은 이미 정의된 클래스를 기반으로 새로운 클래스를 정의하는 것>
#super()는 파이썬에서 상속 관계에서 부모 클래스의 메서드나 인스턴스 변수를 호출할 때 사용하는 함수

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("안녕하세요, 제 이름은 ",self.name," 입니다.")
        print("나이는 ",self.age," 살입니다.")

class Teacher(People): #부모 class를 상속 받음
    def __init__(self, name, age, subject):
        super().__init__(name,age)
        self.subject=subject

    def show_info(self):
        super().introduce()
        print("제 전공은 ",self.subject," 입니다.")

teacher=Teacher("홍길동 ",30," 수학")
teacher.show_info()

#================================================================================================================
#다중 상속 < 다중 상속이란, 하나의 클래스가 여러 개의 부모 클래스를 가질 수 있는 상속 방법을 의미>
class Parent1:
    def method1(self):
        print("Parent1's method1")

class Parent2:
    def method2(self):
        print("Parent2's method2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()  # Parent1's method1
c.method2()  # Parent2's method2

#================================================================================================================
#메서드 오버라이딩(Method Overriding)<부모 클래스의 메서드를 자식 클래스에서 재정의하여 다른 동작을 수행할 수 있도록 하는 것>
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")

# 메서드 오버라이딩을 이용한 다형성 구현
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak() # 각 객체에 따라 다른 동작을 수행

#------------------------------------------------------------------------------------------------------------------
#사칙연산 구현
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

class AdvancedCalculator(Calculator):
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b

c = Calculator()
print(c.add(2, 3))        # 5
print(c.subtract(5, 1))   # 4
print(c.multiply(4, 6))   # 24
print(c.divide(10, 2))    # 5.0

ac = AdvancedCalculator()
print(ac.divide(10, 0))   # Cannot divide by zero
print(ac.divide(10, 2))   # 5.0

#------------------------------------------------------------------------------------------------------------------
#게임 캐릭터 구현(상속 & 매서드 오버라이딩)
class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
    
    def attack(self):
        print(f"{self.name} attacks with a normal attack.")

class Warrior(Character):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health)
        self.strength = strength
    
    def attack(self):
        print(f"{self.name} attacks with a mighty swing.")
    
    def smash(self):
        print(f"{self.name} smashes the ground with a powerful blow.")

class Mage(Character):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic
    
    def attack(self):
        print(f"{self.name} casts a magic missile.")
    
    def teleport(self):
        print(f"{self.name} teleports to a nearby location.")


c = Character("Bob", 10, 100)
c.attack()  # Bob attacks with a normal attack.

w = Warrior("Conan", 20, 200, 15)
w.attack()  # Conan attacks with a mighty swing.
w.smash()   # Conan smashes the ground with a powerful blow.

m = Mage("Merlin", 15, 150, 30)
m.attack()  # Merlin casts a magic missile.
m.teleport()  # Merlin teleports to a nearby location.

#================================================================================================================
#클래스 분리
