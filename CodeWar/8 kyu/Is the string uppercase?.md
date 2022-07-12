# CodeWars Python Solutions

---

## Is the string uppercase?


Is the string uppercase?
Task

Create a method to see whether the string is ALL CAPS.
Examples (input -> output)

"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True

In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.




---

### Given Code


```python
def is_uppercase(inp):
    return False
    pass
```

---

### Solution


```python


def is_uppercase(inp):
    caps = inp.upper()
    if caps == inp:
        return True
    else :
        return False


```

---


[See on CodeWars.com](https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python)
