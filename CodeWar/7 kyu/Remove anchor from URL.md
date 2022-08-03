# CodeWars Python Solutions

---

## Remove anchor from URL


Complete the function/method so that it returns the url with anything after the anchor (#) removed.


**Examples**

```python
# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1'
remove_url_anchor('www.codewars.com?page=1')
```

---

### Given Code


```python
def remove_url_anchor(url):
    # TODO: complete
```



---

### Solution


```python
def remove_url_anchor(url):
    return url.split("#")[0]
```





-------

[See on CodeWars.com](https://www.codewars.com/kata/51f2b4448cadf20ed0000386)
