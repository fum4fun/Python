# CodeWars Python Solutions

---

## Count of positives / sum of negatives


Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].



---

### Given Code


```python
def count_positives_sum_negatives(arr):
    pass
```

---

### Solution


```python
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        if x < 0:
            neg += x
    return [pos, neg]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python)
