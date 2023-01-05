"""matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat3 = []

new_line = []
new_line.append(mat1[2][0])
new_line.append(mat1[1][0])
new_line.append(mat1[0][0])
mat3.append(new_line)
new_line = []
new_line.append(mat1[2][1])
new_line.append(mat1[1][1])
new_line.append(mat1[0][1])
mat3.append(new_line)
new_line = []
new_line.append(mat1[2][2])
new_line.append(mat1[1][2])
new_line.append(mat1[0][2])
mat3.append(new_line)

print(mat3)
"""                             #Це найважча задача з усього шо було. Весь день над нею сидів
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
result = []
for x in range(3):   # Ідея в тому що range(3) це як список із потрібних індексів (0,1,2)
    line = []      #Оновляємо стрінг кожного  разу
    for i in matrix[::-1]:    #Нам треба перевернути матрицю щоб брати числа знизу спочатку типо 741 а не 147
        line.append(i[x])
    result.append(line)
print(result)


