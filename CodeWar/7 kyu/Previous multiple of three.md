# CodeWars Python Solutions

---

## Previous multiple of three

Given a positive integer `n: 0 < n < 1e6`, remove the last digit until you're left with a number that is a multiple of three.

Return `n` if the input is already a multiple of three, and return `null/nil/None` if no such number exists.


**Examples**

```
1      => null
25     => null
36     => 36
1244   => 12
952406 => 9
```


---

### Given Code


```python
def prev_mult_of_three(n):
    pass
```

---



### Solution 


```python
def prev_mult_of_three(n):
    while n % 3:
        n //= 10
    return n or None
```

---




[See on CodeWars.com](https://www.codewars.com/kata/61123a6f2446320021db987d)
