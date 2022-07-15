# CodeWars Python Solutions

---

## Maximum Length Difference

You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).
Example:

a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13

Bash note:

    input : 2 strings with substrings separated by ,
    output: number as a string



---

### Given Code


```python
def mxdiflg(a1, a2):
    # your code
    return -1
```

---

### Solution


```python


def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    x = len(min(a1, key=len))
    y = len(max(a2, key=len))
    result1 = abs(x-y)
    x = len(max(a1, key=len))
    y = len(min(a2, key=len))
    result2 = abs(y-x)
    return result1 if result1 >= result2 else result2


```


---


[See on CodeWars.com](https://www.codewars.com/kata/5663f5305102699bad000056/train/python)
