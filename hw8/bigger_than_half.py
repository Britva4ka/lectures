import math         #Складність 6/10 цікавість 6/10
def bigger_then_half(array): #Задачка наче проста в плані написання коду, але складна в плані зрозуміти який потрібен алгоритм
    array.sort() #Додав цей метод щоб можна була в разнобій числа задавати
    half = math.ceil(len(array) / 2) #ceil округляє в більшу сторону
    for x in array:
        count = 0
        for i in array:
            if x > i:
                count += 1
                if count == half:
                    return x

assert bigger_then_half([1, 2, 3]) == 3# bigger then 2 out of 3
assert bigger_then_half([1, 2, 2, 3]) == 3# bigger then 3 out of 4
assert bigger_then_half([1, 1, 1, 2, 3]) == 2# bigger then 3 out of 5
