#task1
"""
Написати програму Що складає, віднімає, робить скалярний і векторний додаток над векторами
асерти пишите самі
"""
from math import sqrt
class Vector():
    def __init__(self, x:int, y:int, z:int):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other): #Я почитав в інеті що це більше підходить ніж ge.
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
         return False
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def scal_dod(self, other):
        return self.x * other.x+self.y * other.y+self.z*other.z
    def vec_dod(self, other):
        x = self.y * other.z - self.z * other.y     #за формулою в інеті(через матрицю)
        y = -(self.x * other.z - self.z * other.x)
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)
        #return [x, y, z]
    def magnitude(self):
        magnitude = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return round(magnitude, 2) #Не знаю нашо я це зробив. Але я можу отримати величину вектора по модулю.

assert Vector(1, 2, 3).scal_dod(Vector(6, 3, 2)) == 18
assert Vector(1, 2, 3).vec_dod(Vector(6, 3, 2)) == Vector(-5, 16, -9)
assert Vector(-5, 16, -9).magnitude() == 19.03
#task2
"""
Реальзувати метод підрахунку довжин ліній. зробити метод компаре, який буде зрівнювати лінії і казатит яка довша
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
        return f'({p1},{p2})'
    def __eq__(self, other):
        if self.p1 == other.p1 and self.p2 == other.p2:
            return True
        else: return False
    def length(self):
        return sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
    def compare(self, other):             # Method returns a bigger line.
        if self.length() > other.length():
            return self
        elif self.length() < other.length():
            return other
        else: return None
p1 = Point(1, 4)
p2 = Point(2, 9)
p3 = Point(3, 13)
line = Line(p1, p2)
line2 = Line(p1, p3)
print(line.compare(line2))
assert Line(Point(1,4),Point(2,9)).compare(Line(Point(1,4),Point(3,13))) == Line(Point(1,4),Point(3,13))
#task3
"""
В відриві від проекту обміника написати програму через класс, яка складає сумму декількох валют та виводить у іншій.
Для простоти гривня, долар, евро, злотий
"""

class Currency():
    pass

# my_saving = Currency(33, 100, 200, 100)# 4 наших валюти
# my_saving.summary() - виводить мій банк в різних валютах як є
# my_saving.UAH - скільки окрмої валюти
# my_saving.eqvival("UAH") - 33, 100, 200, 100 - загалом в гривнях\чи інших з 4
# my_saving == your_saving - true якщо сумми в еквіваленті рівні
# my_saving + your_saving ....

#task4
"""
typing на клас каренсі та класл Ленс
"""