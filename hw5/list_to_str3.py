def list_to_string(array): #Зробив за хвилину 2/10 по важкості
    string = ''
    for x in array:
        string = string + str(x)
    print(string)
    return string

assert list_to_string(["l", "i", "s", "t"]) == "list"
assert list_to_string(["l", "i", "s", "t", 5, 1.1]) == "list51.1"