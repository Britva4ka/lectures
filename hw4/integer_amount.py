first = int(input('Введите первое число: ')) #Прога що викине усі цілі числа між заданними
second = int(input("Введите второе число: ")) #До речі, 0 завдання було набагато важче, ніж 1 та 2.
count = first + 1
while count != second:
    print(count)
    count = count + 1
# або усе це можна зробити ось так, залежить від того шо нам потрібно
"""
kek = range(first+1, second)
print(list(kek)) #тут ми отримаємо список 
"""
