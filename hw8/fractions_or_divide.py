def divide(a, b):       #Прикольное задание. Мне почему то кажется что я сделал его не так как задумывалось, хз
    if a[-1] == 0 or b[-1] == 0: #Сложность 3/10, интересность 4/10. Математику я в лицее знал хорошо
        return None
    else:
        if a[-1] == b[-1]:
            new_list = [a[0]+b[0], a[-1]]
            for x in range(1, 100)[::-1]:
                if new_list[0] % x == 0 and new_list[1] % x == 0:
                    new_list = [new_list[0]/x, new_list[1]/x]
        elif a[-1] != b[-1]:
            new_list = [a[0]*b[-1]+b[0]*a[-1], a[-1]*b[-1]]
            for x in range(1, 100)[::-1]:
                if new_list[0] % x == 0 and new_list[1] % x == 0:
                    new_list = [new_list[0]/x, new_list[1]/x]
    print(new_list)
    return tuple(new_list)

assert divide((2, 3), (3, 8)) == (25, 24) #16\24 + 9\24 = 25\24 Это уже лично от меня усложнение
assert divide((1, 8), (3, 8)) == (1, 2)#1\8 + 3\8 = 4\8 = 1\2
assert divide((1, 0), (3, 8)) == None#1\0 + 3\8 - not valid