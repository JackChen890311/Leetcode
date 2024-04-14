## 題目參照
 - [top interview](https://leetcode.com/problem-list/top-interview-questions/)
 - [top 100](https://leetcode.com/problem-list/top-100-liked-questions/) 
 - [Grind 75 (No hard, by topic)](https://www.techinterviewhandbook.org/grind75?difficulty=Easy&difficulty=Medium&order=topics)
 - [Neetcode](https://neetcode.io/practice)

## Python 常見操作複雜度
參考 [Python Complexity](https://wiki.python.org/moin/TimeComplexity)
 - `list.sort()`: Tim sort, $O(n\cdot logn)$
 - `set(list)`: $O(n)$
 - `x in set/dict`: $O(1)$
 - `x in list`: $O(n)$
 - set/dict operation: $O(1)$
 - [set difference](https://stackoverflow.com/questions/48044353/what-is-the-run-time-of-the-set-difference-function-in-python): $O(n)$

## 相關重要演算法
- [Fucking Algorithms Github](https://github.com/labuladong/fucking-algorithm) or [Its Website](https://labuladong.github.io/algo/)
- [Dijkstra](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E5%9F%BA%E7%A4%8E%E6%BC%94%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97-graph-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E8%88%87dijkstras-algorithm-6134f62c1fc2)
- [DFS Big-O](https://www.quora.com/Why-is-the-complexity-of-DFS-O-V+E) and [BFS Big-O](https://www.quora.com/Why-is-the-time-complexity-of-BFS-O-V+E)
- [Difference between DFS & BFS](https://www.tutorialspoint.com/difference-between-bfs-and-dfs)
- [Performance comparison between list & deque](https://stackoverflow.com/questions/23487307/python-deque-vs-list-performance-comparison)
- [LRU Cache](https://josephjsf2.github.io/data/structure/and/algorithm/2020/05/09/LRU.html)
## Python Code Snippets
### Basic Data Structure
- [Initialize a 2d matrix](https://www.geeksforgeeks.org/initialize-matrix-in-python/)
    ```python=
    # Correct
    mat = [[0 for _ in range(cols)] for _ in range(rows)]
    mat = [[0] * cols for _ in range(rows)]
    # Wrong
    # mat = [[0] * cols] * rows 
    # mat = [[0 for _ in range(cols)]] * rows
    ```
- [Copy a dictionary](https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy)
	```python=
	d1 = {1 : 2}
	d2 = dict(d1)
	d3 = d1.copy()
	```
-  [Copy a List](https://ithelp.ithome.com.tw/articles/10221255)
	```python=
	a1 = [1, 2, 3]
	# Three different ways to copy a list (Shallow)
	a2 = list(a1)
	a3 = a1.copy()
	a4 = a1[:]
	```
- [Copy a Set](https://stackoverflow.com/questions/23200969/how-to-clone-or-copy-a-set-in-python)
	```python=
	s1 = {1,2,3}
	s2 = set(s1)
	s3 = s1.copy()
	```
- [List](https://docs.python.org/zh-tw/3/tutorial/datastructures.html) and [More about list](https://steam.oxxostudio.tw/category/python/basic/list.html)
    ```python=
    >>> a = [1,2,3,4,5,6,7]
    >>> a[:3]
    [1, 2, 3]
    >>> a[3:]
    [4, 5, 6, 7]
    >>> a[:-3]
    [1, 2, 3, 4]
    >>> a[-3:]
    [5, 6, 7]
    >>> a[-3]
    5
    ```
- Sort a tuple list by sub-element
	```python
	>>> a = [(1,3),(2,2),(4,5),(6,0),(0,-1)]
	>>> print(sorted(a, key = lambda x: x[0]))
	[(0, -1), (1, 3), (2, 2), (4, 5), (6, 0)]
	>>> print(sorted(a, key = lambda x: x[1]))
	[(0, -1), (6, 0), (2, 2), (1, 3), (4, 5)]
	```
- [Nonlocal vs global](https://stackoverflow.com/questions/33211272/what-is-the-difference-between-non-local-variable-and-global-variable)
- [Nonlocal vs global 2](https://ktinglee.github.io/LearningPython100days(6)_global_and_nonlocal/)
- [Typing](https://docs.python.org/zh-tw/3/library/typing.html)
### [Collections](https://docs.python.org/zh-tw/3/library/collections.html)
- collections.defaultdict
    ```python=
    >>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    >>> d = defaultdict(set)
    >>> for k, v in s:
    ...    d[k].add(v)
    ...
    >>> sorted(d.items())
    [('blue', {2, 4}), ('red', {1, 3})]
    ```
- [collections.OrderedDict](https://ithelp.ithome.com.tw/articles/10193794)
- [collections.ChainMap](https://ithelp.ithome.com.tw/articles/10193794)
- [collections.Counter](https://docs.python.org/zh-tw/3/library/collections.html#counter-objects)
	```python=
	>>> c = Counter('gallahad')                 # a new counter from an iterable
	>>> c
	Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
	>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
	>>> c
	Counter({'red': 4, 'blue': 2})
	>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args
	>>> c
	Counter({'dogs': 8, 'cats': 4})
	```
- collections.deque
	- Used for [[Stack]] and [[Queue]]
    ```python=
    from collections import deque
    D = deque()
    D.append(1)
    D.appendleft(2)
    _ = D.pop()
    _ = D.popleft()
    print(D[0])
    print(D[-1])
    ```


