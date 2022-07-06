# CodeWars Python Solutions

---

## Dot Calculato


You have to write a calculator that receives strings for input. The dots will represent the number in the equation. There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.

Here are the following valid operators :

---

### Given Code

```python
def calculator(txt):
    # This is the place to code!
    pass
```

---

### Solution

```python
def calculator(txt):
    a = txt.split(" ")
    x = len(a[0])
    z = len(a[2])
    y = a[1]
    s = 0
    if y == '+':
        s = x + z
    if y == '-':
        s = x - z
    if y == '*':
        s = x * z
    if y == '//':
        s = x // z
    i = s * '.'
    return i
```


---


[See on CodeWars.com](https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/python)
