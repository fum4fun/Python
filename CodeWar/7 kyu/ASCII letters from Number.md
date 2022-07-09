# CodeWars Python Solutions

---

## ASCII letters from Number


You have to create a function that converts integer given as string into ASCII uppercase letters.

All ASCII characters have their numerical order in table.

---

### Given Code

```python
def convert(number):
    pass
```

---

### Solution

```python
def convert(number):
    return "".join([chr(int(number[e:e+2])) for e in range(0,len(number),2)])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/589ebcb9926baae92e000001/train/python)
