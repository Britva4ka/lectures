import json

def get_curr_course(path:str="currency_course.json") -> dict :
    """
    returns curr course json in dictionary type.
    :param path:
    :return:
    """
    with open(path, 'r') as file:
        return json.load(file)

def tablo(course: dict) -> str:
    """
    Returns the table with information about course and currency.
    :param course:
    :return:
    """
    tablica = (f'\t{"BUY":*<13}{"UAH":*^6}{"SELL":*>13}\n\t')
    for cur in course['UAH']['buy']:
            tablica += (f'{course["UAH"]["buy"][cur]:-<13.2f}{cur:-^6}{course["UAH"]["sell"][cur]:->13.2f}\n\t')
    tablica += (f'{"*":*^32}')
    return tablica


def bank_calc(result: float, value: str, path:str="bank.json") -> float: #added bank calculation
    """
    This script count if u have enough banknotes (bank.json) to give needed amount of cash.
    It returns amount of cash that u can give. Used banknotes automaticly removes.
    :param result:
    :param value:
    :param path:
    :return:
    """
    with open(path, 'r') as file:
        bank = json.load(file)[value]
        sum = 0
        for x in bank:
            sum = sum + bank[x] * int(x)    #Можно сделать чтобы функция перезаписывала данные в банке джсон.(на будущее)
        if result < sum:       #И можно сделать типо чтоб пользователь вводил купюры и их добавляло, аналогично с отниманием
            count = 0       #И реализовать фишку можно типо пользователь дает 200 долларов говорит надо 170 поменять.
            for x in bank:  #Если мне не будут вырубать свет в 09 и врубать в 01, то может когда то руки дойдут.
                if result/int(x) >= 1 and bank[x] >= result/int(x):
                    new = result//int(x)   #НУ соответсвенно можно еще сделать так чтобы предлагало округлять и тп.
                    result = result%int(x) #Но мы это уже делали
                    bank[x] = bank[x] - new
                    count += new * int(x)
            return count
        elif result > sum:
            return sum

# TODO має бути можливисть робити знижку чи змінною чи манімуляцією з mul
#Потім зроблю
def cal_cell_course(cource:dict, mul:float) -> dict:
    """
    Function that updates SELL course in currency_course.json with multiplayer
    :param cource:
    :param mul:
    :return:
    """
    for curr_name in cource.keys():
        for sec_curr, rate in cource[curr_name]["buy"].items():
            cource[curr_name]["sell"].update({sec_curr: round(rate * (1 + mul), 2)})
    return cource


def exchange(amount:float, cource:dict, operation:str, old_curr:str, new_curr:str) -> float:
    """
    The main exchanger script. Returns The needed amount of cash.
    :param amount:
    :param cource:
    :param operation:
    :param old_curr:
    :param new_curr:
    :return:
    """
    return amount * cource[old_curr][operation][new_curr]

# TODO якщо помилиться користувач то ввести знову.....
#Потом зроблю

def input_data(data:tuple, count:int=0, result:list=[]) -> list:
    """
    Function that goes settings and ask user questions. Answers collected in result.
    :param data:
    :param count:
    :param result:
    :return:
    """
    # result = []
    # count = 0
    while count < len(data):
        if data[count]['question']:
            input_value = input(data[count]['question'])
            if input_value == 's': #Це я робив до лекції де ми передивлялись обмінник. Не буду прибирати, буде чесно
                input_value = 'sell'
            if input_value == 'b':
                input_value = 'buy'
            if input_value == "reset":
                result = []
                count = 0
            elif input_value == "back":
                if not result:
                    continue
                else:
                    result.pop()
                    count -= 1
                    while not data[count]['question']:
                        result.pop()
                        count -= 1
            else:
                if data[count]["func"]:
                    input_value = float(input_value)
                result.append(input_value)
                count += 1
        else:
            result.append(data[count]["fixture"])
            count += 1
    return result
