"""В бескінечном уциклі ви вводите числа. кожне чьотне число додається до загальної суми. кожне нечьотне віднімається.
при написанні слова end цикл зупиняється і видається сума."""
sum = 0              #2/10 по важкості. По цікавості 3/10. Це було б інтересно 2 заняття тому, а так дуже легко.
while True:
    num = input('Введите число или end: ')
    if num == 'end':
        break
    else:
        num = float(num)
        if num % 2 == 0:
            sum += num
        elif num % 2 == 1:
            sum -= num
print(sum)