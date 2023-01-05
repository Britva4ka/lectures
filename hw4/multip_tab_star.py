num = int(input('Insert the number(1 - 16): '))
if 1 <= num <= 16:
    for x in range(1, 10):
        print('\n')
        for i in range(num-4, num+4):
            print(f'{x:2} * {i:2} = {x * i:3}', end=' ')#І тут я зрозумів що можна було використовувати змінну
else:                                              #типу str = '' => str = str + f'{}'... як на лекції ви показували
    print('Incorrect Insert')                               #Але мені здається з end набагато простіше