import json

def get_curr_course(path="currency_course.json"):
    with open(path, 'r') as file:
        return json.load(file)

def tablo(course: dict) -> str:
    tablica = (f'\t{"BUY":*<13}{"UAH":*^6}{"SELL":*>13}\n\t')
    for cur in course['UAH']['buy']:
            tablica += (f'{course["UAH"]["buy"][cur]:-<13.2f}{cur:-^6}{course["UAH"]["sell"][cur]:->13.2f}\n\t')
    tablica += (f'{"*":*^32}')
    return tablica


def bank_calc(result: float, value: str, path="bank.json") -> float: #added bank calculation
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
def cal_cell_course(cource, mul):
    for curr_name in cource.keys():
        for sec_curr, rate in cource[curr_name]["buy"].items():
            cource[curr_name]["sell"].update({sec_curr: round(rate * (1 + mul), 2)})
    return cource


def exchange(amount, cource, operation, old_curr, new_curr):
    return amount * cource[old_curr][operation][new_curr]

# TODO якщо помилиться користувач то ввести знову.....
#Потом зроблю

def input_data(data, count=0, result=[]):
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
