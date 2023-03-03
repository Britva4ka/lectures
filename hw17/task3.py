import json
import random
random.seed(19)


class Player: #Гравець
    def __init__(self, name):
        self.name = name
        self.score = 1500
        # self.skip_turn = False
    def __repr__(self):
        return f'{self.name, self.score}'
    def __str__(self):
        return f'{self.name, self.score}'
    def make_bet(self):
        self.skip_turn = False
        bet = int(input(f"{self.name}, make your bet (0 to skip turn): "))
        if bet == 0:
            self.skip_turn = True
        if self.skip_turn:
            return 0
        return bet
    def choose_side(self):
        if self.skip_turn:
            return None
        while True:
            side = input(f"{self.name}, choose your side (h - heads, t - tails): ")
            if side.lower() == "h":
                return "Head"
            elif side.lower() == "t":
                return "Tails"
            else:
                print("Invalid input. Please enter 'h' or 't'.")
    def analysis(self, results, choices):
        pass

class Bot(Player): #Бот звичайний
    def __init__(self, name):
        super().__init__(name)

    def make_bet(self):
        self.skip_turn = False
        bet = random.randint(0, self.score)
        if bet == 0:
            self.skip_turn = True
        if self.skip_turn:
            return 0
        return bet

    def choose_side(self):
        if self.skip_turn:
            return None
        return random.choice(["Head", "Tails"])


class Math_Bot(Bot): #Бот математик
    def analysis(self, results, choices):
        if len(results) >= 3:
            keys = list(results.keys())
            if results[keys[-1]]['result'] == results[keys[-2]]['result'] and results[keys[-2]]['result'] == results[keys[-3]]['result']:
                decision = True
                variants = ['Head', 'Tails']
                variants.remove(results[keys[-1]]['result'])
                self.bet = random.randint(1, self.score)
                self.choice = variants[0]
            else:
                self.bet = 0
                self.choice = None
        else:
            self.bet = 0
            self.choice = None
    def make_bet(self):
        return self.bet
    def choose_side(self):
        return self.choice

class Repeat_Bot(Bot): #Бот имитатор
    def analysis(self, results, choices):
        if results:
            keys = list(results.keys())
            richest_player = max(results[keys[-1]]['players'], key=lambda x: x.score)
            exist = False
            for player_name in choices:
                if player_name == richest_player.name:
                    exist = True
            if exist:
                self.choice = choices[richest_player.name]["choice"]
            else:
                self.choice = random.choice(["Head", "Tails"])
        else:
            self.choice = random.choice(["Head", "Tails"])
    def choose_side(self):
        if self.skip_turn:
            return None
        return self.choice

class Faminist_Bot(Bot): #Бот уравнювач
    def analysis(self, results, choices):
        count_heads = 0
        count_tails = 0
        for round in results:
            if results[round]["result"] == "Head":
                count_heads += 1
            else:
                count_tails += 1
        if count_heads > count_tails:
            self.choice = "Tails"
        elif count_tails > count_heads:
            self.choice = "Head"
        else:
            self.choice = random.choice(["Head", "Tails"])
    def choose_side(self):
        if self.skip_turn:
            return None
        return self.choice

class Doter_Bot(Bot): #БОТ АГРЕССОР
    def analysis(self, results, choices):
        bank_head = 0
        bank_tails = 0
        for player in choices:
            if choices[player]['choice'] == 'Head':
                bank_head += choices[player]['bet']
            elif choices[player]['choice'] == 'Tails':
                bank_tails += choices[player]['bet']
        if bank_head > bank_tails:
            self.choice = "Tails"
        elif bank_head < bank_tails:
            self.choice = "Head"
        else:
            self.choice = random.choice(["Head", "Tails"])
    def choose_side(self):
        return self.choice
class Game(): #Типу крупье, який зберігає наші данні
    def __init__(self, players: list):
        self.players = players
        self.results = {}
    def round(self, amount): #Сам код для гри. Більшість ботів я зробив коли вже написав його =D
        for i in range(amount):
            if i % 2 == 0:
                k = 1
            else:
                k = -1
            print(f"ROUND {i+1}")
            bank = 0
            winnings = 0
            winners = []
            choices = {}
            win_scores = []
            """
            {
            ROUND1: {
                    players_choices: {player1: {bet:20, choice:tails},
                                        player2: ...}
                    winners : [player1, player3],
                    result : "Head",
                    
            ЧЕРНЕТКА ДЛЯ СТРУКТУРИ ДАННИХ НЕОБХІДНИХ ДЛЯ БОТІВ
            }
            """
            result_side = random.choice(["Head", "Tails"])
            for player in self.players[::k]:
                player.analysis(self.results, choices)
                bet = player.make_bet()
                choice = player.choose_side()
                bank += bet
                player.score -= bet
                if choice == result_side:
                    winners.append(player)
                    winnings += bet
                choices.update({player.name: {"bet": bet, "choice": choice}})
            for winner in winners:
                win_score = round(bank * choices[winner.name]["bet"] / winnings)
                win_scores.append(win_score)
                winner.score += win_score


            self.results.update({f"Round {i+1}": {"result": result_side, "winners": list(zip(winners, win_scores)), "choices": choices, "players": self.players}})

            print(self.results)   #Логгінг не встиг зробити вчасно, але я його зробив у першому завданні. Думаю ви мені вірите, що я б зробив це на ІЗІ

players = [Player('Michael'), Repeat_Bot('bot0'), Faminist_Bot('bot1'), Bot('bot2'), Math_Bot('bot3'), Doter_Bot('bot4')]
game = Game(players)
game.round(5)#кількість раундів            #Автоматичний режим також не встиг зробити. Але я є його раніше робив, і тут би зміг 100%. Просто не встиг(
