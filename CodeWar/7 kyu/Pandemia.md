# CodeWars Python Solutions

---

## Pandemia


**Description:**

β οΈ The world is in quarantine! There is a new pandemia that struggles mankind. Each continent is isolated from each other but infected people have spread before the warning. β οΈ

πΊοΈ You would be given a map of the world in a type of string:

```
s = "01000000X000X011X0X"

"0" : uninfected

"1" : infected

"X" : ocean
```

β« The virus can't spread in the other side of the ocean.

β« If one person is infected every person in this continent gets infected too.

β« Your task is to find the percentage of human population that got infected in the end.

βοΈ Return the percentage % of the total population that got infected.

ββ The first and the last continent are not connected!


π‘ **Example:**

```
start: map1 = "01000000X000X011X0X"
end:   map1 = "11111111X000X111X0X"
total = 15
infected = 11
percentage = 100*11/15 = 73.33333333333333
```

β For maps without oceans "X" the whole world is connected.

β For maps without "0" and "1" return 0 as there is no population.



---

### Given Code


```python
def infected(s):
    # Code
```

---

### Solution


```python
def infected(s):
    cons = s.split("X")
    tot = 0
    inf = 0
    for c in cons:
        tot += len(c)
        if "1" in c:
            c = c.replace("0", "1")
        inf += c.count("1")
    return 100 * inf / tot if inf > 0 else 0
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5e2596a9ad937f002e510435)
