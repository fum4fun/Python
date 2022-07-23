# CodeWars Python Solutions

---

## Quarter of the year


Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.



---

### Given Code

```Python

def quarter_of(month):
    pass
```

---

### Solution
```Python
def quarter_of(month):
    if month < 4:
        return 1
    elif month < 7:
        return 2
    elif month < 10:
        return 3
    else: 
        return 4
```

-------

[See on CodeWars.com](https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python)
