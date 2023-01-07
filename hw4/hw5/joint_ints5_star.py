def join_ints(my_list):       #Дуже цікава задачка, але я сходу зрозумів в яку сторону думати.
    my_list.reverse()         #Але все одно хвилин 15 витратив на цю лялечку. Тому навіть не знаю. 6-7/10
    ints = 0              #Не бачив сенсу робити перший варіант з переводом в string, тому що це легше
    counter = 1
    for x in my_list:                 #Друга частина другого завдання була сама важка, як на мене.
        if type(x) == int:
            ints = ints + x*counter
            counter= counter*10
    print(ints)
    return ints


assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143