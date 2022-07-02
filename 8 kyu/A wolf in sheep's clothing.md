# CodeWars Python Solutions

---

## A wolf in sheep's clothing


If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.


---

### Given Code

def warn_the_sheep(queue):
    pass

---

### Solution

def warn_the_sheep(queue):
    queue = queue[::-1]
    wolf_counter = None
    for i, animal in enumerate(queue):
        if animal == 'wolf':
            wolf_counter = i
    if wolf_counter == 0:
        return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {wolf_counter}! You are about to be eaten by a wolf!'


-------

[See on CodeWars.com](https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python)
