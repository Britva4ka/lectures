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
mat2 = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
result = []
for x in range(3):   # Ідея в тому що range(3) це як список із потрібних індексів (0,1,2)
    line = []      #Оновляємо стрінг кожного  разу
    for i in matrix[::-1]:    #Нам треба перевернути матрицю щоб брати числа знизу спочатку типо 741 а не 147
        line.append(i[x])
    result.append(line)
#print(result)
titles_list = ["input", "needed", "result"]

for i in range(len(titles_list)):
    titles_list[i] = titles_list[i].ljust(13, " ")

print(*titles_list) #Не знав шо можна розпаковувать списки

for i, j, k in zip(matrix, mat2, result): #Трохи зрозумів, але не дуже. як працює функція ZIP
    print(i," | ", j, " | ", k)


print("*" * 38)
if result == mat2:
    print("Problem solved!")
else:
    print("Wrong answer!")

