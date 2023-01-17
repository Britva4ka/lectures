import csv
import json
def my_func(boxes):             #Складність оцінюю 10\10 і цікавість 10\10.
    return boxes[3]
'''
Завдання із зірочкою. Якщо б математику в школі не вчив - не виконав би.
Спочатку я намагався знайти найбільшу коробку за середнім значенням висоти ширини та довжини, але потім зрозумів
що це лажа. Тому що може бути коробка 9999999/1/9999999. значення буде великим, але коробка 1/2/1 не влізе. 
Але зрозуміло одне. Що коробка з більшим обємом не влізе вкоробку з меншим.
Тому зробив функцію my func для використання в key метода sort. (підгледів в інеті).
Список коробок сортував по обєму і намагався засунути в саму велику за обємом коробку інші коробки
Але до кофеїн та цукор в моїй крові підказали мені, що з обємом така ж сама фігня як з розмірами може бути 999/1/999
І до мене дійшло, що можна перевірити інші коробки, окрім першої. Тому я 
просто зробив цикл в циклі, який намагаєтся засунути якомога більше коробок в
кожну коробку по черзі. Функція matreshka повертає варіант з найбільшим успіхом.
Цього разу зробив як ви казали. Спочатку імпорти, потім функції, потім інше.
'''
def matreshka(box_sizes):
    box_sizes.sort(key=my_func, reverse=True)  # Прийшлось шукати інфу в інеті, бо не знав як сортувати за елементом
    numbers_of_variatons = []
    for x in box_sizes:
        matreshka = [x, ]
        for i in box_sizes:
            if i[0] < x[0] and i[1] < x[1] and i[2] < x[2]:
                matreshka.append(i)
        numbers_of_variatons.append(len(matreshka))
    return max(numbers_of_variatons)

#basic csv read.
# with open("kaki.csv") as file:
#     csvfile = csv.reader(file)
#     for row in csvfile:
#         print(row)# list with 1 string since we dont set csv dialect
#         print(row[0])#print that string directly
with open("kaki.csv") as file:
    csvfile = csv.reader(file, delimiter='\t')
    with open('kaki2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        count = 0
        heigh = []
        length = []
        with_ = []
        capacity = []
        box_sizes = []
        for row in csvfile:
            #print(row)# list of 3 elements, since i passed \t as separator
            #print(row[0])#first el of th list
            if count == 0:
                row.append('capacity')
                count += 1
                writer.writerow(row)
            else:
                row.append(int(row[0])*int(row[1])*int(row[2]))
                box_sizes.append(row)
                heigh.append(int(row[0]))
                length.append(int(row[1]))
                with_.append(int(row[2]))
                capacity.append(int(row[3]))
                count += 1
                writer.writerow(row)
            print(row)
aver_heigh = round(sum(heigh) / (count-1), 2)
aver_len = round(sum(length) / (count-1), 2)
aver_with = round(sum(with_) / (count-1), 2)
aver_capac = round(sum(capacity) / (count-1), 2)
average = {
    'heigh': aver_heigh,
    'length': aver_len,
    'with': aver_with,
    'capacity': aver_capac,
}
print('\n')
print(average)
print('\n')
print(matreshka(box_sizes))
with open("average_size.json", "w") as json_file:
    json.dump(average, json_file)