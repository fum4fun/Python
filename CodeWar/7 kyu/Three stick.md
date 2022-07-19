# CodeWars Python Solutions

---

## Three sticks


Imagine that you are given two sticks. You want to end up with three sticks of equal length. You are allowed to cut either or both of the sticks to accomplish this, and can throw away leftover pieces.

Write a function, maxlen, that takes the lengths of the two sticks (L1 and L2, both positive values), that will return the maximum length you can make the three sticks.

---

### Given Code


def maxlen(L1,L2):
  pass


---

### Solution


def maxlen(L1,L2):
    ma = max(L1, L2)
    mi = min(L1, L2)
    if ma - mi - mi - mi > 0: return ma/3
    if ma - mi - mi > 0: return mi 
    return ma/2



---


[See on CodeWars.com](https://www.codewars.com/kata/57c1f22d8fbb9fd88700009b/train/python)
