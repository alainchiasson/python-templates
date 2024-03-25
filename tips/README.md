# Tips for Python.

From : https://www.youtube.com/watch?v=qUeud6DvOWI

25 nooby Python hab its you need to ditch. There is experience in Python vs other languages and 
are actually pretty good. The video is from 2022, so it may also have some outdated stuff.

1. Use f-strings - makes formating easier.
2. Use with statements with files so they can be closed on exceptions.
3. Everything that must be closed (eg: sockets) has acontext manager that works as above. So don't use try: finally: for sockets.
4. Using a bare except clause ( except: ) - always trap somethihng ( except: Exception ) or better ( except: TheRealException )
5. Power opertor is not like other languages.
6. Default Mutable arguments in call stack

def bad_append(n , l=[]):
    l.append(n)
    return l

def good_append(n , l=None):
    if l is None:
        l = []
    l.append(n)
    return l

Defaults are defined at function creation. Since l is a mutable type, it becomes shared.

l1 = bad_append(0) # [0]
l2 = bad_append(1) # [0,1]

l3 = good_append(0) # [0]
l4 = good_append(1) # [1]

7. Using comprehensions - and not just list comprehemsions. There is List, dict, and others.
8. Comprehensions should not be used everywhere. Use where appropriate.
9. do not chack for class type with ==, use isinstance()
10. use == for None, True and False - use is. 
11. 
12. 

Using range(len(a))

```python
a = [1,2,3]
b = ['one','two','three']

# Not pythonic 
for i in range(len(a)):
    v = a[i]

# Pythonic
for v in a:
    ...

# Also - if you want index and value
for i, v in enumerate(a):
    ...


# Not pythonic
for i in range(len(b)):
    av = a[i]
    bv = b[i]

for av, bv in zip(a, b):
    ...

for i, (av, bv) in enumerate(zip(a,b)):
    ...

```

13. Looping over dict keys.

d = {"a":1, "b":2, "c":3 }

# Don't
for key in d.keys():
    ...

# Default is keys
for key in d:
    ...

# If modifying dict 
for key in list(d.keys()):
    ...

# Or even
for key in list(d):
    ...

14. Dictionary items method.

d = {"a":1, "b":2, "c":3 }

# Do this 
for key in d:
    val = d[key]

# Do this 
for key, val in d.itmes():
    ...

15. tuple unpacking

# Works
mytup = 1,2
x = mytup[0]
y = mytup[1]

# Better
x,y = mytup

16. Using a 0+ counter in a loop. See Enumerate above.

17. Timing code. Use time.perf-counter()

18. Use Logging module instead of print.

def main():
    level = loggin.DEBUG
    fmt = '[%(levelname)s] %(asctime)s = %(message)s'
    loggin.basicConfig(level=level, format=fmt)

logging.debug("debug info")
logging.info("Just some info")
logging.error("uh oh !!")

19. Using shell=tru in subprocess instead of array of command ( not sure what this is.)
20. Doing real math in raw python. Use NumPy or Pandas.
21. Import *
22. Learn how path imports - package install in env.
23. Python is partially compiled.
24. not following PEP-8 - its a style guide, follow it.
25. Anything with Python2 - always do python3