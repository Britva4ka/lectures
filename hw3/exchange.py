USD = 39.92
EUR = 39.20
PLN = 8.44
PROX_COEF = 0.05
usdsell = USD + USD*0.05
eursell = EUR + EUR*0.05
plnsell = PLN + PLN*0.05
print(f'\t{"BUY":*<13}{"SELL":*>13}\n\t'
      f'{USD:-<10.2f}{"USD":-^6}{usdsell:->10.2f}\n\t'
      f'{EUR:-<10.2f}{"EUR":-^6}{eursell:->10.2f}\n\t'
      f'{PLN:-<10.2f}{"PLN":-^6}{plnsell:->10.2f}\n\t'
      f'{"*":*^26}')
choose = input('Купити чи продати валюту?Введіть B або S:').title()
if choose == 'B':
    val_buy = input('Оберіть валюту, яку хочете купити (USD, EUR, PLN): ').upper() #Метод щоб вводити можна було маленькими також
    val_uah = float(input("Введіть кількість гривень, яку ви хочете продати: "))
    if val_buy == 'EUR':
        currency = eursell
        result = val_uah // currency
        remain = round(val_uah % currency,2)
        print(f"{'Ваша кількість євро:':<25} {result:>5}\n{'Ваша решта гривень:':<25} {remain:>5}")
    elif val_buy == 'USD':
        currency = usdsell
        result = val_uah // currency
        remain = round(val_uah % currency,2)
        print(f"{'Ваша кількість доларів:':<25} {result:>5}\n{'Ваша решта гривень:':<25} {remain:>5}")
    elif val_buy == 'PLN':
        currency = plnsell
        result = val_uah // currency
        remain = round(val_uah % currency, 2)
        print(f"{'Ваша кількість злотих:':<25} {result:>5}\n{'Ваша решта гривень:':<25} {remain:>5}")
    else:
        print('Не вірно обрана валюта.')
    if 50 < (result % 50) * PROX_COEF + (result % 50): #Це частина коду, яка відповідає за пропозицію округлити сумму
        add_amount = 50 - result % 50              #Сподіваюсь не дуже хардкод, зробив як зрозумів.
        new_result = add_amount + result
        add_uah = round(add_amount * currency - remain, 2)
        choose2 = input(f'Чи бажаете внести ще {add_uah} грн щоб отримати рівно {new_result}?(Y/n):').title()
        if choose2 == 'Y':
            print(f'Отримайте {new_result}, дякуєм шо обрали нас.')
        elif choose2 == 'N':
            print('Як хочете, двічі не пропонуємо.')
        else:
            print('Не вірно обрана операція.')  # Було б круто якщо б повертало на крок назад
    elif 0 > result % 50 - (result % 50 + 50) * PROX_COEF and not result % 50 == 0: #and щоб не спрацьовувало коли рівно 50
        rem_amount = result % 50
        new_result = result - rem_amount
        rem_uah = round(rem_amount * currency + remain, 2)
        choose2 = input(f'Чи бажаєте ви отримати рівно {new_result} та решту {rem_uah}?(Y/N):').title()
        if choose2 == 'Y':
            print(f'Отримайте: {new_result}.Ваша решта: {rem_uah}.Дякуєм шо обрали мене.')
        elif choose2 == 'N':
            print('ДА ПАБАЧЕННЯ')
        else:
            print('Не вірно обрана операція.')  # Хотів би дізнатись як повернути користувача на минулий етап
    else:
        print("З Новим Роком!")
elif choose == 'S':                             # Це частина коду для продажу валюти за гривні.
    val_choose = input('Оберіть валюту, яку хочете продати (USD, EUR, PLN): ').upper()
    val_sell = float(input("Введіть кількість валюти, яку ви хочете продати: "))
    if val_choose == 'EUR':
        result = val_sell * EUR
        print(f"Ваша кількість гривень: {result}")
    elif val_choose == 'USD':
        result = val_sell * USD
        print(f"Ваша кількість гривень: {result}")
    elif val_choose == 'PLN':
        result = val_sell * PLN
        print(f"Ваша кількість гривень: {result}")
    else:
        print('Не вірно обрана валюта.')
else:
    print('Не вірно обрана функція.')
# Знизу наброски варіанту де можна спростити код, але я дуже втомився.
"""#Обмінник нового покоління beta
USD = 39.92
EUR = 39.20
PLN = 8.44
usdsell = USD + USD*0.05
eursell = EUR + EUR*0.05
plnsell = PLN + PLN*0.05
print(f'\t{"BUY":*<13}{"SELL":*>13}\n\t'
      f'{USD:-<10.2f}{"USD":-^6}{usdsell:->10.2f}\n\t'
      f'{EUR:-<10.2f}{"EUR":-^6}{eursell:->10.2f}\n\t'
      f'{PLN:-<10.2f}{"PLN":-^6}{plnsell:->10.2f}\n\t'
      f'{"*":*^26}')
text = input('Оберіть що ви хочете зробити у такому форматі (BUY/SELL *AMOUNT* *VALUTA*):').lower()
choose, amount, val = text.split()
if choose == 'buy':

elif choose == 'sell':

else:
    print('Incorrect operation')"""

