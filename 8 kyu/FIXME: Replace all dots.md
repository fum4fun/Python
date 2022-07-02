# CodeWars Python Solutions

---

## A Needle in the Haystack


Definition

The code provided is supposed replace all the dots . in the specified String str with dashes -

But it's not working properly.

---

### Given Code

'''python
import re
def replace_dots(str):
    return re.sub(r".", "-", str)
'''


---

### Solution

'''python
def replace_dots(str):
    return str.replace(".", "-")
'''


---


[See on CodeWars.com](https://www.codewars.com/kata/596c6eb85b0f515834000049/train/python)
