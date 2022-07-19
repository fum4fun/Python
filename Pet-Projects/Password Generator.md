## Password Generator
```pyton
import random


def ran_pas():
    pas = ''
    for x in range(num):
        pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return pas


num = int(input('Длина пароля '))
col = int(input('Количество паролей '))
for i in range(col):
    print(ran_pas())
```
