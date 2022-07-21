import random


def ran_pas():
    pas = ''
    for x in range(num):
        pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return pas


num = int(input('Длина пароля: \n '))
col = int(input('Количество паролей: \n '))
for i in range(col):
    print(f'Пароль № {i+1}: ', ran_pas())

