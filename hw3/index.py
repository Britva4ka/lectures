'''
ft inch mile - фут дюйм Миля
stone ,lb,oz - стоун фунт унция
5'10'' 5 ft 10 inch                #Це мої чернетки. Не видаляю, бо вдруг вирішу модернізувати код якось
m = ft/3,281
m = inch/39,37
kg = 2,205 * lb

'''
height = input('Enter your height:')
weight = input('Enter your weight:')
if height.find(','):
    height = height.replace(',','.')
if weight.find(','):
    weight = weight.replace(',','.')
height = height.strip() #Код работает и без стрипа. Но лишним он не будет :)
weight = weight.strip()
if height.endswith('ft'): #Проверка на американку
    height = height[:height.find('ft')] #Ищем и отрезаем буквы
    height = float(height) / 3.281 #Переводим цифры во флот и переводим в систему СИ
elif height.endswith('cm'):
    height = float(height[:height.find('cm')])
    height = height / 100
if weight.endswith('lb'):
    weight = float(weight[:weight.find('lb')])
    weight = weight / 2.205
elif weight.endswith('kg'):
    weight = float(weight[:weight.find('kg')])
else:
    print('incorrect magnitude')                        #Можна додати будь яку кількість величин для переводу.
print(round(weight/height**2, 2))


