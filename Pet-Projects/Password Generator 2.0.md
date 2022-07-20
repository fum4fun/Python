## Password Generator

```python
import random
import string


def generate_password(*args):
    password = []
    length = n
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = [lower, upper, num, symbols]
    for i in range(length):
        password.append(random.choice(all[random.randint(0, 3)]))
    return ''.join(password)


n = int(input('Длина пароля: '))
print(generate_password())
```
