import math
import logging
import json
import random
logging.basicConfig(filename='story.log', encoding='utf-8', level=logging.DEBUG)
random.seed(19)
logging.basicConfig(
        level=logging.DEBUG,
        format = "%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="story.log"
    )
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

def game(players:list, count):
    bank = 0
    winnings = 0
    winners = []
    players_dict = []
    result = random.choice(['head', 'tails'])
    logging.info(f"COIN FLIPS AND RESULT IS {result}")
    for player in players:
        bank += player.bet
        if player.choice == result:
            winnings += player.bet
    for player in players:
        if player.choice == result and player.bet != 0:
            # winners.append(player.name)
            win_amount = round(player.bet / winnings * bank)
            player.change_points(win_amount)
            logging.info(f"{player} wins {win_amount}")
        # players_dict.append(vars(player))

        # if player.points == 0:
        #     players.remove(player)
        #     print(f"{player} - ВЫБЫВАЕТ")
    # story = {"ROUND": count-1, "PLAYERS": players_dict, "RESULT": result, "WINNERS": winners},
    # with open('story.json', 'a') as f:
    #     json.dump(story, f, indent=2)
    #     f.write(',')
    print(result, players)
    return result, players


PLAYER = Player('Michael', 1500)
bots_list = create_bots(10)
#Снизу доделать, сверху не трогать. Реализовать повтор 100 раз. Функцию АВТО. Запись игр. Вылет игроков. Валидацию.
#Идеи: функция/цикл вайл/цикл фор.+
auto = False
count = 1
logging.info("Game started.")
while count < 101:
    # players_list = bots_list + [PLAYER]
    if PLAYER.points == 0:
        logging.warning(f"{PLAYER} LOSE. HAHA")
        break
    if len(bots_list) == 0:
        logging.warning(f"{PLAYER} WON")
        break
    logging.info(f"ROUND {count}")
    for bot in bots_list:
        if bot.points == 0:
            bots_list.remove(bot)
            logging.warning(f"{bot} ВЫБЫВАЕТ. Закончились очки.")
        else:
            bot.made_bet(random.randint(0, bot.points))
            logging.info(f"{bot} make a bet {bot.bet}")
            bot.made_choice(random.choice(['head', 'tails']))
            logging.info(f"{bot} make a choice {bot.choice}")


    players_list = bots_list + [PLAYER]

    if not auto:
        todo = input(f"You have {PLAYER.points}, what's your next move?(bet, auto)?: ")
        while todo not in ['bet', 'auto']:
            todo = input(f"Incorrect input. You have {PLAYER.points}, what's your next move?(bet, auto)?: ")
        if todo == 'bet':
            bet, choice = input(f"Make your bet (points and side) (100 head/tails): ").split()
            PLAYER.made_bet(int(bet))
            PLAYER.made_choice(choice)
            #TODO validate
        elif todo == 'auto':
            bet, choice, num = input(f"Make your bet for next rounds (points/side/number of moves): ").split()
            num = int(num)
            PLAYER.made_bet(int(bet))
            PLAYER.made_choice(choice)
            auto = True
        count += 1
    else:
        if PLAYER.points < int(bet):
            bet, choice = input(f"U have not enough points ({PLAYER.points}). Make new bet: (points side) ").split()
            auto = False
        if num == 1:
            auto = False
        PLAYER.made_bet(int(bet))
        PLAYER.made_choice(choice)
        num -= 1
        count += 1
    logging.info(f"{PLAYER} makes bet {PLAYER.bet} on {PLAYER.choice}")

    game(players_list, count)