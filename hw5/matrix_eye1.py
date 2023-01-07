def eye_matrix(size):       #Цікаве завдання, 5/10 по важкості
    matrix = []
    for x in range(size):
        line = []
        for i in range(size):
            line.append(0)
        line[x] = 1
        #line[-x-1] = 1 Це я додавав другу діагональ. Чомусь я подумав що вона тут потрібна
        matrix.append(line)
    print(matrix)
    return matrix

assert eye_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert eye_matrix(4) == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]







#[1 0 1]
#[0 1 0]
#[1 0 1]
"""
[ 1 0 0 1]
[ 0 1 1 0]
[ 0 1 1 0]
[ 1 0 0 1]

[ 1 0 0 0 1]
[ 0 1 0 1 0]
[ 0 0 1 0 0]
[ 0 1 0 1 0]
[ 1 0 0 0 1]
"""
