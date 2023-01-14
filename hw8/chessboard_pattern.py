def chesboard_pattern(width, height): #Складніть 5/10, цікавість 5/10
    chesboard = []
    for x in range(height):
        line = []           #Забув про обмінник сказати в минулому ДЗ, цікавість 10/10, складність 9/10.
        for i in range(width):                   #Я б навіть ще його якось доробив. Прикольно. Багато ідей в голову лізе
            line.append(1)
            if i % 2 == 0 and x % 2 == 0: #Цю частину коду я взагалі чисто на автоматі написав і воно спрацювало.
                line[i] = 0
            elif i % 2 == 1 and x % 2 == 1:
                line[i] = 0
        chesboard.append(line)
    print(*chesboard, sep='\n')
    return chesboard

assert chesboard_pattern(2, 2) == [[0, 1], [1, 0]]
assert chesboard_pattern(4, 3) == [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]