password = input('Введите пароль: ')
length = False #Задаем нужніе нам параметрі как фолс
upper = False
lower = False
sym = False
num = False
symbols = '!@/?' # символи які потрібні бути в паролі
for x in password:
    if 'A' <= x <= 'Z':
        upper = True
    elif 'a' <= x <= 'z':       #Тут прикол в тому що, наші параметри стануть тру, якщо хоча б один елемент співпаде
        lower = True
    elif "0" <= x <="9":
        num = True
    elif x in symbols:
        sym = True

if len(password) >= 12:
    length = True

if length and upper and lower and sym and num == True:
    print('Пароль безопасен.')
else:
    print("Пароль - говно полное.")


