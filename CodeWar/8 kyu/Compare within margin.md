# CodeWars Python Solutions

---

## Compare within margin


**Definition**

Create a function close_compare that accepts 3 parameters: a, b, and an optional margin. The function should return whether a is lower than, close to, or higher than b.

a is considered "close to" b if margin is greater than or equal to the distance between a and b.

Please note the following:

    When a is close to b, return 0.

Otherwise...

    When a is less than b, return -1.

    When a is greater than b, return 1.

If margin is not given, treat it as zero.

Assume: margin >= 0

Tip: Some languages have a way to make parameters optional.


```Python
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```

should return `"found the needle at position 5"`

---

### Given Code


```python
def close_compare(a, b, margin):
    pass
```

---

### Solution


```python
def close_compare(a, b, margin=0):
    if a == b or abs(a - b) <= margin:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1
```

---


[See on CodeWars.com](https://www.codewars.com/kata/56676e8fabd2d1ff3000000c)
