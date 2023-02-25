#task1
"""
написати програму яка бере з папки за датою з файлу hw.py бере домашне завдання і розкладає шаблони
і умови домашок за файлами
Використовуйте  # символ як орієнтир що нове завдання почалось.
"""
import pathlib
p = pathlib.Path(__file__)
p2 = p.parent.joinpath("homework_tasks")
for child in p2.iterdir():
    for file in child.iterdir():
        with file.open("r") as f:
            content = f.read()
            tasks = content.split(sep= "#task")[1:]
            for i, task in enumerate(tasks):
                with open(f"{child}\\task_{i + 1}.py", "w") as new_file:
                    new_file.write(task[1:])
                    #ЭТОТ КОД ОДНОРАЗОВЫЙ. Я И ТАК ЗАПУТАЛСЯ ПОКА ЕГО ПИСАЛ. Сделать его многоразовым в ТЗ не входило :)

#task2
"""
переписати скріпт який ми написали на лекції(створення файлів з датами)

так щоб. Якщо файл існує - не переписувати його
назви файлів має бути в форматі дата-місяці-рік
"""
import datetime
p = pathlib.Path(__file__)
working_path = p.parent.joinpath("lecture_14")
if not working_path.exists():
    working_path.mkdir()
start = datetime.date(2023, 1, 1)
for day in range(31):
    date = (start + datetime.timedelta(days = day)).strftime("%d-%m-%Y")
    if not working_path.joinpath(date).exists():
        working_path.joinpath(date).touch()
#task3
"""
написати скрипт, який видаляє всі файли, які відповідають суботі та неділі
"""
from datetime import datetime
for child in working_path.iterdir():
    datetime_str = child.name
    datetime_object = datetime.strptime(datetime_str, "%d-%m-%Y").isoweekday()
    if datetime_object > 5:
        child.unlink()
