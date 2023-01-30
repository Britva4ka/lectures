def flatten(array):
    list1 = []
    for i in array:
        if type(i) == list:
            list1.extend(flatten(i))
        else:
            list1.append(i)
    return list1
assert flatten([1,[2], [3,[6]]]) == [1, 2, 3, 6]
assert flatten([[[[]]]]) == []
