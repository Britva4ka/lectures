#task1
"""розрзаховувалась вагова категорі бійця
додати до рекорду бійця поразку чи перемогу, нічию
написати красивий репр
Збобити десь інтсанців боксерів з випадковими величинами ростру, ваги, рекордів, віку
,nickname - 5 реальних боесерів 5 імен тварин 5 прикметників
"""
import random
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