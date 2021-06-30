With counter, we can quickly count for items, how many times it occurs.


```
 l = ["a","b","c","a"]
 
>>> import collections
>>> count = collections.Counter(l)
>>> count
Counter({'a': 2, 'b': 1, 'c': 1})

>>> count.most_common(2)
[('a', 2), ('b', 1)]

```
