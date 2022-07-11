# CodeWars Python Solutions

---

## Find Nearest square number


Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.

---

### Given Code
```python
def nearest_sq(n):
``` 

---

### Solution
```python
def nearest_sq(n):
    import math
    m = round(math.sqrt(n))
    return m * m
```    


-------

[See on CodeWars.com](https://www.codewars.com/kata/5a805d8cafa10f8b930005ba/train/python)
