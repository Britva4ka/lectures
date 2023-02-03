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
    def magnitude(self)->float:
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
        return f'({self.p1},{self.p2})'
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

assert Line(Point(1,4),Point(2,9)).compare(Line(Point(1,4),Point(3,13))) == Line(Point(1,4),Point(3,13))



#task3
"""
В відриві від проекту обміника написати програму через класс, яка складає сумму декількох валют та виводить у іншій.
Для простоти гривня, долар, евро, злотий
"""

class Currency():
    def __init__(self, x:int=0 ,y:int=0, z:int=0, t:int=0):
        self.bank = {'uah': x, 'usd': y, 'eur': z, 'pln': t}
        # self.uah = x
        # self.usd = y
        # self.eur = z
        # self.pln = t
    def __eq__(self, other)->bool:
        if self.show_equivalent() == other.show_equivalent():
            return True
        else: return False
    def __str__(self):
        return f'{self.bank}'
    def __add__(self, other):
        x = self.bank['uah'] + other.bank['uah']
        y = self.bank['usd'] + other.bank['usd']
        z = self.bank['eur'] + other.bank['eur']
        t = self.bank['pln'] + other.bank['pln']
        return Currency(x, y, z, t)
    def show_all(self):
        return f'Hryvnas: {self.bank["uah"]}, Dollars: {self.bank["usd"]}, Euros: {self.bank["eur"]}, Zloti: {self.bank["pln"]}'
    def show_one(self, key:str='uah'):
        return self.bank[key.lower()]
    def show_equivalent(self, key:str='uah', course:dict={"USD": 40, "EUR": 36, "PLN": 6}) -> float:
        eq_uah = 0
        # course = {          #Можна зсилатись на датабазу якусь
        #     "USD": 40,
        #     "EUR": 36,
        #     "PLN": 6
        # }
        for x, y in self.bank.items():
            if x == 'uah':
                eq_uah += y
            else :
                eq_uah += y*course[x.upper()]
        if key == 'uah':
            return round(eq_uah, 2)
        else:
            return round(eq_uah/course[key.upper()], 2)


lol=Currency(33, 100, 200, 100)
assert lol.show_all() == "Hryvnas: 33, Dollars: 100, Euros: 200, Zloti: 100"
assert lol.show_one('usd') == 100
assert lol.show_equivalent('eur') == 328.69
assert bool(lol==Currency(33, 100, 200, 100)) == True
assert bool(lol==Currency(32, 100, 199, 100)) == False
assert lol + Currency(20, 10, 15, 12) == Currency(53, 110, 215, 112)



#task4
"""
typing на клас каренсі та класл Ленс
"""
class Lenth():
    metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }

    def __init__(self, value:float, unit:str = "m"):
        self.value = value
        self.unit = unit

    def converToMeters(self) -> float:
        return self.value * self.metric[self.unit]

    def __add__(self, other):
        lenth_meter = self.converToMeters() + other.converToMeters()
        return Lenth(lenth_meter/Lenth.metric[self.unit], self.unit)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __ge__(self, other):
        return max(self.converToMeters(), other.converToMeters())

    def __str__(self):
        return str(self.converToMeters()) + "m"

    def __repr__(self):
        return f"Lenth {self.value} {self.unit}"
#
#
# val = Lenth(5, "yd")
# val2 = Lenth(4, "ft")
#
# val3 = val + val2 #Lenth(n, "yd")
# print(val3.__repr__())
# print(val >= val2)
#

