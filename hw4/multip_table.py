num = int(input('Введіть число від 1 до 100: '))
if 1 <= num <= 100:
    for i in range(1, 100):
        result = num * i
        print(f'{num} * {i} = {result}')
else:
    print('Incorrect insert')