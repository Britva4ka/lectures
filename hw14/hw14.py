import math
import random
random.seed(19)
class Player():
    def __init__(self, name: str, points: int):
        self.points = points
        self.name = name

    def __repr__(self):
        return f'({self.name}, {self.points}, {self.bet}, {self.choice})'

    def __str__(self):
        return f'({self.name}, {self.points})'
    def change_points(self, amount):
        self.points += amount

    def made_bet(self, bet):
        self.bet = bet
        self.points -= bet

    def made_choice(self, choice):
        self.choice = choice
def create_bots(amount):
    bots = []
    for x in range(amount):
        bot = Player(f'bot{x}', random.randint(1000, 2000))
        bots.append(bot)
    return bots

def game(players:list):
    bank = 0
    winners = []
    winnings = 0
    result = random.choice(['head', 'tails'])
    for player in players:
        bank += player.bet
        if player.choice == result:
            winnings += player.bet
    for player in players:
        if player.choice == result:
            player.change_points(round(player.bet / winnings * bank))
    print(result, players)
    return result, players


PLAYER = Player('Michael', 1500)
bots_list = create_bots(10)
#Снизу доделать, сверху не трогать. Реализовать повтор 100 раз. Функцию АВТО. Запись игр. Вылет игроков. Валидацию.
#Идеи: функция/цикл вайл/цикл фор.+
auto = False
count = 0
while count < 100:
    if PLAYER.points == 0:
        print("U LOSE. HAHA")
        break
    print(f"ROUND {count}")
    for bot in bots_list:
        if bot.points == 0:
            bots_list.remove(bot)
            print(f"{bot} ВЫБЫВАЕТ")
        else:
            bot.made_bet(random.randint(0, bot.points))
            bot.made_choice(random.choice(['head', 'tails']))

    players_list = bots_list + [PLAYER]

    if not auto:
        todo = input(f"You have {PLAYER.points}, what's your next move?(bet, auto)?: ")
        while todo not in ['bet', 'auto']:
            todo = input(f"Incorrect input. You have {PLAYER.points}, what's your next move?(bet, auto)?: ")
        if todo == 'bet':
            bet, choice = input(f"Make your bet (points and side) (100 head/tails)").split()
            PLAYER.made_bet(int(bet))
            PLAYER.made_choice(choice)
            #TODO validate
        elif todo == 'auto':
            bet, choice, num = input(f"Make your bet for next rounds (points/side/number of moves").split()
            num = int(num)
            PLAYER.made_bet(int(bet))
            PLAYER.made_choice(choice)
            auto = True
        count += 1
    else:
        if PLAYER.points < int(bet):
            bet, choice = input(f"U have not enough points ({PLAYER.points}). Make new bet: (points side)").split()
            auto = False
        if num == 1:
            auto = False
        PLAYER.made_bet(int(bet))
        PLAYER.made_choice(choice)
        num -= 1
        count += 1

    game(players_list)




#task1
"""
seed(19) використовуємо для рандому щоб у всіх було однаково.
Підкидається монетка орел\рішка
Гравець мав депозит очок.
Гравець може зробити ставку на випадок 100 1 - 100 на решку
Додати якусь кількість конкурентів ботів які також можть рботити ставки.
Вигриаєте то сумма банку розподіляжться до цілих між гравцями що вгадали.
100 кидкив монетки.
Записали в файл історію гри

"""

#task 2

"""classmethod для прямокутника з двох точок створеного(діагональ)"""
#task3
"""
зробити метод валідації статік методом
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
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def compare(self, other):  # Method returns a bigger line.
        if self.length() > other.length():
            return self
        elif self.length() < other.length():
            return other
        else:
            return None


class Shape():

    def __init__(self):
        pass

    def __str__(self):
        pass
    def calc_per(self):
        pass
    def calc_area(self):
        pass
class Rectangle(Shape):

    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    @classmethod
    def two_points(cls, p1, p3):
        p2 = Point(p3.x, p1.y)
        p4 = Point(p1.x, p3.y)
        return cls(p1, p2, p3, p4)

    @staticmethod
    def validate(p1, p2, p3, p4):
        if p1.y == p2.y and p1.x == p4.x and p3.y == p4.y and p3.x == p2.x\
        and p1 != p2:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.p1}, {self.p2}, {self.p3}, {self.p4}'

    def __eq__(self, other):
        if self.p1 == other.p1 and self.p2 == other.p2 and self.p3 == other.p3 and self.p4 == other.p4:
            return True
        else: return False

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

assert Rectangle.two_points(Point(1, 1), Point(4, 0)) == Rectangle(Point(1, 1), Point(4, 1), Point(4, 0), Point(1, 0))
assert Rectangle.two_points(Point(1, 1), Point(4, 0)).validate(Point(1, 1), Point(4, 1), Point(4, 0), Point(1, 0)) == True