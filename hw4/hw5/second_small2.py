
"""def second_smallest(array):      #З використанням методів та функцій.
    array.remove(min(array))        #Це легко 2/10 по важкості
    print(min(array))
    return min(array)

second_smallest([2, 9, 1,])"""
def second_smallest(array):        #Або завдання важке, або я дуже тупий. важкість ставлю 7-9/10
    minimal = min(array)
    min2 = max(array)
    for x in array:
        if min2 > x > minimal: #Спочатку я ще думав шо не можна built in функції використовувати, то взагалі сидів тупив.
            min2 = x    #Потів перечитав і побачив що не можна тільки методи. Це полегчило задачу, але все одно складно
    print(min2)
    return min2



assert second_smallest([1, 2, 2, 3]) == 2
assert second_smallest([-1, 10, -2, 2]) == -1