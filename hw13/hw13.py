#task1
"""розрзаховувалась вагова категорі бійця
додати до рекорду бійця поразку чи перемогу, нічию
написати красивий репр

ВОТ ТО ЧТО НИЖЕ Я ВООБЩЕ НЕ ПОНЯЛ ЧТО ОТ МЕНЯ ТРЕБУЕТСЯ

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
    """ВАГОВА
    КАТЕГОРІЯ.РЕПР.РЕКОРД.NICKNAME"""
    def __init__(self, style, record, nickname):
        # super().__init__(name, last_name, age)
        self.style = style
        self.record = record
        self.nickname = nickname
    # def __repr__(self):
    #     return f'MEET AN AWESOME {self.name} {self.nickname}, {self.weight} KG, WINSTREAK {self.record} IN A RAW'


class Boxer(Person, Fighter):
    def __init__(self, name, last_name, age, style, record, nickname):
        Person.__init__(self, name, last_name, age)
        Fighter.__init__(self, style, record, nickname)

    def set_weight(self, weight):
        super().set_weight(weight)
        if self.weight < 70:
            self.category = 'lightweight'
        elif self.weight < 110:
            self.category = 'middleweight'
        else:
            self.category = 'bigfatweight'
    def __repr__(self):
        return f"AN AWESOME {self.name} {self.nickname}, IN A {self.category.upper()} ON A {self.record} WINSTREAK"

lol = Boxer('Michael', 'Dombrovan', 21, 'kek', 500, "BRITVA")
lol.set_weight(100)
print(lol.__repr__())
nicknames = ['Britva', 'Lezvie', 'kakashka', 'lekvidator', 'scorpion']
surnames = ['kek1', 'kek2', 'kek3', 'kek4', 'kek5']
names = ['leprikon', 'dosada', 'imbicil', 'yashirka', 'kloun']
styles = ['lol1', 'lol2', 'lol3', 'lol4', 'lol25']
boxer = Boxer(random.choice(names), random.choice(surnames), random.randint(20, 50), random.choice(styles), \
    random.randint(0, 100), random.choice(nicknames))
boxer.set_weight(random.randint(60, 150))
print(boxer.__repr__())

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

    def __init__(self):
        pass

    def __str__(self):
        pass
    def calc_per(self):
        pass
    def calc_area(self):
        pass

class Circle(Shape):

    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2
        self.r = Line(p1, p2)
    def calc_per(self):
        return round(2*math.pi * self.r.length(), 2)
    def calc_area(self):
        return round(math.pi * self.r.length()**2, 2)
    def is_circle(self):
        if self.p1 == self.p2:
            return False
        else:
            return True
c = Circle(Point(1, 2), Point(2, 3))
print(c.calc_area(), c.calc_per(), c.is_circle())


class Rectangle(Shape):

    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def calc_area(self):
        return Line(self.p1, self.p2).length() * Line(self.p1, self.p4).length()

    def calc_per(self):
        return 2 * (Line(self.p1, self.p2).length() + Line(self.p1, self.p4).length())
    def is_rectagle(self):
        if self.p1.y == self.p2.y and self.p1.x == self.p4.x and self.p3.y == self.p4.y and self.p3.x == self.p2.x\
        and self.p1 != self.p2:
            return True
        else:
            return False

r = Rectangle(Point(1, 1), Point(4, 1), Point(4, 0), Point(1, 0))
print(r.is_rectagle(), r.calc_per(), r.calc_area())

class Squeare(Rectangle):

    def is_squeare(self):
        r = Rectangle(self.p1, self.p2, self.p3, self.p4)
        if r.is_rectagle() and Line(self.p1, self.p2).length() == Line(self.p2, self.p3).length():
            return True
        else:
            return False

s = Squeare(Point(1, 1), Point(2, 1), Point(2, 0), Point(1, 0))
print(s.is_squeare(), s.calc_per(), s.calc_area())

class Triangle(Shape):
    def __init__(self, p1:Point, p2:Point, p3:Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calc_per(self):
        return round(Line(self.p1, self.p2).length() + Line(self.p3, self.p2).length() + Line(self.p1, self.p3).length(), 2)

    def calc_area(self):
        p = self.calc_per() / 2
        return round(math.sqrt(p * (p - Line(self.p1, self.p2).length()) * Line(self.p3, self.p2).length() * \
                         Line(self.p1, self.p3).length()), 2)

    def is_triangle(self):
        if self.calc_area() == 0:
            return False
        else:
            return True

t = Triangle(Point(1,3), Point(4, 6), Point(-2, -7))
print(t.calc_per(), t.calc_area(), t.is_triangle())