# CodeWars Python Solutions

---

## Sort array by string length

Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

For example, if this array were passed as an argument:

`["Telescopes", "Glasses", "Eyes", "Monocles"]`

Your function would return the following array:

`["Eyes", "Glasses", "Monocles", "Telescopes"]`

All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length.

---

### Given Code


```python
def sort_by_length(arr):
    pass
```

---



### Solution 


```python
def sort_by_length(arr):
    i = 0
    sorted_arr = []
    while len(sorted_arr) != len(arr):
        for item in arr:
            if len(item) == i:
                sorted_arr.append(item)
        i += 1
    return sorted_arr
```

-------

[See on CodeWars.com](https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c)
