# CodeWars Python Solutions

---

## Powers of 2



Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

---

### Given Code
```pyhon
def powers_of_two(n):
    return []
```
---

### Solution
```pyhton
def powers_of_two(n):
    out = []
    for i in range(n+1):
        out.append(2**i)
    return out
```

-------

[See on CodeWars.com](https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python)
