currency_courses = {
    "UAH": {
            "USD": 39.92,
            "EUR": 39.20,
            "PLN": 8.44},
    "USD": {                               #ЭТА ПРОГРАММА РАССЧИТАНА НА ЮЗЕРА ЧТО НОРМАЛЬНО ВВОДИТ ДАННЫЕ.
            "UAH": 0.025,           #Я могу сделать типо вы не правильно ввели. Но код и так огромный
            "EUR": 0.98,
            "PLN": 0.21},
}
def curr_rate(sellval, buyval):
    rate_sell = round(currency_courses[sellval][buyval] * 1.05, 2)
    return rate_sell
                  #Тут достаточно долго обьяснять что я сделал. Запустите программу и посмотрите. Думаю прикольно вішло
while True: #Шоб программа бесконечно повторялась.
    sellval, amount = input('Выберите валюту что хотите продать. И ее кол-во (UAH 1000)\nДоступны ' + str(list(currency_courses))).upper().split()
    print(f'\t{"BUY":*<10}{sellval:*^6}{"SELL":*>10}')
    count = 0
    for x in currency_courses[sellval]:
        print(f'\t{currency_courses[sellval][x]:-<10.2f}{list(currency_courses[sellval])[count]:-^6}{curr_rate(sellval, x):->10.2f}')
        count += 1
    print(f'\t{"*":*^26}')
    buyval = input('Выберите валюту что хотите получить (USD)\nДоступны ' + str(list(currency_courses[sellval]))).upper()
    bank = {
        "USD": {100 : 100, 50: 20, 10: 10, 5:0, 1:0 }, #Тут кількість купюр можна міняти, там знизу я все круто зробив
        "EUR": {100 : 100, 50: 20, 10: 10, 5:0, 1:0 }, # 50 - номінал : 20 - кількість.
        "PLN": {100 : 100, 50: 20, 10: 10, 5:0, 1:0 },
        "UAH": {100 : 100, 50: 20, 10: 10, 5:0, 1:0 },
    }
    val = currency_courses[sellval][buyval]
    valsell = curr_rate(sellval, buyval)
    def convertation(amount, valsell):
        result = float(amount) // valsell
        remain = round(float(amount) % valsell, 2)
        return result, remain

    def value_check(): #Я можу загорнути весь той шлак знизу у функцію, але чесно кажучи не бачу сенс. Може я не правильно зрозумів завдання.
        pass           #Або не правильно зрозумів сенс создання функцій. Сподіваюсь дійдемо розуміння на наступній лекції.
    kek = convertation(amount, valsell)
    print(f'Вы получаете: {kek[0]} {buyval}\n'
              f'Ваша сдача: {kek[1]} {sellval}')
    reshta = kek[0]
    sum = 0
    for x in bank[buyval]: #Знизу мій персональний витвір мистецтва. Я не знаю яким чином я це зробив, але я це зробив.
         sum = sum + bank[buyval][x]*x
    if reshta < sum:
        for x in bank[buyval]:
            if reshta/x >= 1 and bank[buyval][x] >= reshta/x:
                new = reshta//x
                reshta = reshta%x
                bank[buyval][x] = bank[buyval][x] - new
        #print(bank) #ЦЕ Я ВИКОРИСТОВУВАВ ДЛЯ ПЕРЕВІРКИ. Мені так було легше зрозуміти шо я написав
        #print(reshta)       #Можете теж спробувати, так буде легше зрозуміти шо я таке незрозуміле зробив
        if reshta == 0:
            print('Спасибо і до побачення')
        elif reshta > 0:
            lol = input(f'У банку недостатньо купюр щоб видати вам {buyval}. Пропонуєм спростити сумму на {reshta} {buyval}.\n'
                  f'Ви отримаєте {kek[0]-reshta} {buyval} та решту {round(kek[1]+reshta*valsell, 2)} {sellval}. Y/N?').upper()
            if lol == "Y":
                print("Отримайте ваші гроші. Дякую до побачення")
            elif lol == "N":
                print('Ну тоді гуляй фраєрок.')
    elif reshta > sum:
        chebureck = input(f'У банка недостатньо купюр шоб виплатити вам усі ваші гроші.\n'
                          f'Можемо дати вам максимум {sum} {buyval} і повернем вам {round((reshta-sum)*valsell, 2)} {sellval}. Y/N?').upper()
        if chebureck == 'Y':
            print("Візміть ваши гроші і до побачення")
        elif chebureck == 'N':
            print("Баба з возу - коням легше.")
