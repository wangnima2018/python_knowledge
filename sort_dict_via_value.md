https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

```
dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

```

```
>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> sorted_x = sorted(x.items(), key=lambda kv: kv[1])
>>> sorted_x
[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]. # this is list of tuples
>>> dict(sorted_x)
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
```
