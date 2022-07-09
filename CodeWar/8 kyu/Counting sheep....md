# CodeWars Python Solutions

---

## Counting sheep...


Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

---

### Given Code
```python
def count_sheeps(sheep):
  # TODO May the force be with you
  pass
```
---

### Solution
```python
def count_sheeps(sheep):
    return sum([1 for s in sheep if s])
 ```   


-------

[See on CodeWars.com](https://www.codewars.com/kata/54edbc7200b811e956000556/train/python)
