# CodeWars Python Solutions

---

## Will there be enough space?



Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.
---

### Given Code
```python
def enough(cap, on, wait):
```
---

### Solution
```python
def enough(cap, on, wait):
    a = on + wait
    if cap >= a:
        return 0
    if a > cap:
        return a - cap
```    


-------

[See on CodeWars.com](https://www.codewars.com/kata/5875b200d520904a04000003/train/python)
