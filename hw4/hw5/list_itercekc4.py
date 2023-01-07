def list_intercection(list1, list2):      #Тут треба було трохи посидіти, але норм. 3-4/10 по важкості.
    list = []
    for x in list1:
        for i in list2:
            if i == x:
                list.append(i)
                list1.remove(i)
                list2.remove(i)
    if list == []:
        return None
    print(list)
    return list

assert list_intercection([1, 1, 1, 2], [1, 3, 4]) == [1, ]
assert list_intercection(["foo", 1, "bar"], [2, 3, 4]) == None
assert list_intercection(["foo", 1, "bar"], []) == None
assert list_intercection(["foo", 1, "bar"], [4, "foo", 7]) == ["foo", ]