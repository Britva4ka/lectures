#task1
"""розрзаховувалась вагова категорі бійця
додати до рекорду бійця поразку чи перемогу, нічию
написати красивий репр
Збобити десь інтсанців боксерів з випадковими величинами ростру, ваги, рекордів, віку
,nickname - 5 реальних боесерів 5 імен тварин 5 прикметників
"""
import random
import math
class Person():

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):#Lenth
        self.height = height

    def calculate_mbi(self):
        bmi = self.weight / pow(self.height.converToMetric(), 2)
        return bmi

    def __str__(self):
        return f"{self.name} {self.last_name} {self.age}"

    def __repr__(self):
        return f"{self.name} {self.last_name} is {self.age} y.o"


class Fighter():

    def __init__(self):
        self.style
        self.record
        self.nickname




class Boxer(Person, Fighter):
    pass

#tack 2
"""
Написати програму яка будує прямокутник(вершини), коло за заданими точками(центр і точка на колі в вм=ипаду кола), трикутник
кожна фігура має вміти рахувати периметр, площу, та перевірку на правильність введених вершин
"""
class Point():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else: return False

class Line():
    def __init__(self, point1:Point, point2:Point):
        self.p1 = point1
        self.p2 = point2
    def __str__(self):
        return f'({self.p1},{self.p2})'
    def __eq__(self, other):
        if self.p1 == other.p1 and self.p2 == other.p2:
            return True
        else: return False
    def length(self):
        return math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
    def compare(self, other):             # Method returns a bigger line.
        if self.length() > other.length():
            return self
        elif self.length() < other.length():
            return other
        else: return None
class Shape():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

class Circle(Shape):

    def __init__(self, name, p1:Point, p2:Point):
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.r = Line(p1, p2)
    def calc_per(self):
        return 2*math.pi * self.r.length()
    def calc_area(self):
        return math.pi * self.r.length()**2
c = Circle('kaki', Point(1, 2), Point(2, 3))
print(c.calc_area(), c.calc_per())

class Rectangle(Shape):

    def __init__(self, name, height, width):
        self.height = height
        self.width = width
        super().__init__(name)

    def calc_area(self):
        return self.height*self.width

class Squeare(Rectangle):

    def __init__(self,name, height):
        super().__init__(name, height, height)