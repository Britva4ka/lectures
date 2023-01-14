def sum_list(array): #На перший погляд задачка проста, але з типом прийшлось запаритись.
    sum = 0           #Складніть 3/10. Цікавість 6-7/10
    for x in array:
        sum += float(x)
    if sum.is_integer(): #Це знайшов в документації прикріленній к другому заняттю. Это ли вы имели в виду?
        return int(sum)
    else:
        return sum
assert sum_list([1, 2, "1"]) == 4
assert type(sum_list([1, 2, "1"])) == int
assert sum_list([1, 2, "1", "1.1"]) == 5.1
assert type(sum_list([1, 2, "1", "1.1"])) == float
assert sum_list([1, 2, "1", "-1.0"]) == 3
assert type(sum_list([1, 2, "1", "-1.0"])) == int