# CodeWars Python Solutions

---

## Return the day


Complete the function which returns the weekday according to the input number:

---

### Given Code
```python
def whatday(num):
```
---

### Solution
```python
def whatday(num):
    if num == 1:
        return "Sunday"
    if num == 2:
        return "Monday"
    if num == 3:
        return "Tuesday"
    if num == 4:
        return "Wednesday"
    if num == 5:
        return "Thursday"
    if num == 6:
        return "Friday"
    if num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"
 ```  


-------

[See on CodeWars.com](https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python?collection=codeschool-beginner)
