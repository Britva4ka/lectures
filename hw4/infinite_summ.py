print('Вводіть цифри, программа видасть вам сумму цих чисел.'
      '\nЩоб завершити ввод - напишіть end')
numbers = ''
count = 1
finish = 0
while numbers != 'end':
    numbers = input(f'Введіть {count} число:')
    count = count + 1
    if numbers == 'end':
        break
    finish = finish + float(numbers)
print(finish)
