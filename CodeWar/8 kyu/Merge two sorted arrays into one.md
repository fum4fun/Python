# CodeWars Python Solutions

---

## Merge two sorted arrays into one


You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.
---

### Given Code

```python
def merge_arrays(arr1, arr2):
  return
```

---

### Solution

```python
def merge_arrays(arr1, arr2):
    arr3 = arr1 + arr2
    arr3 = list(set(arr3))
    arr3.sort()           
    return arr3
    
```



---


[See on CodeWars.com](classroom.google.com/u/1/c/MTk2NDMxOTM2MjQ3)
