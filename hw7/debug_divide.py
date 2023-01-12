start = 8
end = 15

denominator = [2, 3]
div_count = []#[[8,10], [3, 12]]


# ДЗ довести до кінця цю програму
for denom_index in range(len(denominator)):
    div_list = []
    for num in range(start, end):
        if num%denominator[denom_index] == 0:
            div_list.append(num)
    div_count.append(div_list)

    #Я ТАК И НЕ ПОНЯЛ ПОЧЕМУ ВЫДАВАЛО ОШИБКУ out of range. я пробовал в индекс добавить -1([denom_index - 1]) и оно
    #работало. Получалось добавляло соответственно по индексам сначала -1 и потом 0. (одно и тоже).В любом случае прога
    #теперь работает и вполне нормально и даже проще вішло. СНИЗУ КАК БЫЛО. СВЕРХУ КАК Я СДЕЛАЛ
"""for num in range(start, end):
    for denom_index in range(len(denominator)):
        if num % denominator[denom_index]:
            if len(div_count) <= denom_index:
                if len(div_count) == 0:
                    div_count.append(list())
                div_count[denom_index].append(num) 
            else:
                div_count.append(list())"""
    # if i % 2 == 0:
    #     div_2.append(i)
    # if i % 3 == 0:
    #     div_3.append(i)
print(div_count)
for num in div_count:
    print(*num[0:10])