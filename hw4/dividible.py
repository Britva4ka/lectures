kek = True #змінна що відповідає за корректність вводу юзером інформації та дає йому другий шанс
while kek:
    print("Введіть два числа від 1 до 200.")
    a = int(input('Перше число: '))          #Спочатку я зробив різні цикли, для ділення на 2, 3, 4 і тд
    b = int(input('Друге число: '))          #А потім я допер як можна застовувати цикл в циклі.
    if 1 <= a <=200 and 1 <= b <= 200:
        numbers = list(range(a+1, b))
        count = 0
        for i in range(2, 7):
            print(f'Dividible by {i}:', end=' ') #До речі: я не знав як їх викидати в один рядок
            count = 0                            #Тому я глянув штуку END в інеті. Сподіваюсь це законно
            for x in numbers:
                if x%i == 0:
                    count = count + 1         #Каунт зупиняє програму шоб вона виводила тільки перші 10 чисел у рядок
                    print(f"{x:3}", end=',')
                if count == 10:
                    break
            kek = False
            print('\n')
    else:
        print('Я же казав вводити від 1 до 200. Дурень')