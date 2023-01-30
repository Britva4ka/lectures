#  add bank calculation
#  додати табличку з курсами
# TODO заппропонувати ще покращення обміника
#В банк_калк() записав ідеі.
"""
+) Беремо звідкісь ззовні курс покупки
+) Розраховуємо курс продажу
?) Мати змогу Міняти націнку, чи робити знижку
+) Мати змогу обмінювати різні валюти в майбутьому але зараз лише відносно гривні
) Мати змогу міняти операцію купівля\продаж
) Мати змогу в командному промті написати ресет і почати опитування знову, в майбутьному написати бек і переввезти
минуле значення при цьому зберігаючи старе
) Мати змогу виводити на екран табло з курсом валют
) чи можемо видати чи ні. (банк)

"""

from settings import INPUT_QUESTIONS
from utils import get_curr_course, cal_cell_course, exchange, input_data, bank_calc, tablo

# говоритиь що тут в нас скрипт який тре виконати
if __name__ == "__main__":
    cource = get_curr_course()
    cource = cal_cell_course(cource, 0.05)
    # amount = 1600
    # operation = "sell"
    # old_curr = "UAH"
    # new_curr = "USD"
    # result = exchange(amount, cource, operation, old_curr, new_curr)
    # print(f"I will {operation} {amount} {new_curr} for {old_curr} {result}")

    print(tablo(cource)) #таблиця

    amount, op, old_curr, new_curr = input_data(INPUT_QUESTIONS)
    new_ammount = exchange(amount, cource, op, old_curr, new_curr)
    if op == "sell":
        req_bank = new_curr
        req_amount = amount
    elif op == 'buy':
        req_bank = old_curr
        req_amount = new_ammount
    print(f"we will {op} {amount} {new_curr} for {new_ammount} {old_curr}")
    print(f'we can {op} {bank_calc(req_amount, req_bank)}')