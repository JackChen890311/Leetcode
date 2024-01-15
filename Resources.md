## 題目參照
 - [top interview](https://leetcode.com/problem-list/top-interview-questions/)
 - [top 100](https://leetcode.com/problem-list/top-100-liked-questions/) 
 - [Grind 75 (No hard, by topic)](https://www.techinterviewhandbook.org/grind75?difficulty=Easy&difficulty=Medium&order=topics)

## Python 常見操作複雜度
參考 [Python Complexity](https://wiki.python.org/moin/TimeComplexity)
 - `list.sort()`: Tim sort, $O(n\cdot logn)$
 - `set(list)`: $O(n)$
 - `x in set/dict`: $O(1)$
 - `x in list`: $O(n)$
 - set/dict operation: $O(1)$
 - [set difference](https://stackoverflow.com/questions/48044353/what-is-the-run-time-of-the-set-difference-function-in-python): $O(n)$

## 相關重要演算法
- [Fucking Algorithms Github](https://github.com/labuladong/fucking-algorithm)
- [Dijkstra](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E5%9F%BA%E7%A4%8E%E6%BC%94%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97-graph-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E8%88%87dijkstras-algorithm-6134f62c1fc2)
- [DFS Big-O](https://www.quora.com/Why-is-the-complexity-of-DFS-O-V+E) and [BFS Big-O](https://www.quora.com/Why-is-the-time-complexity-of-BFS-O-V+E)
- [Difference between DFS & BFS](https://www.tutorialspoint.com/difference-between-bfs-and-dfs)

# TODO (Add in Topics Later)
- [Python heapq 介紹](https://ithelp.ithome.com.tw/articles/10247299)

- [3 ways to iterate BST](https://shubo.io/iterative-binary-tree-traversal/)
- In-order traversal (left -> mid -> right) will give you sorted list!

- [Binary search](https://medium.com/appworks-school/binary-search-%E9%82%A3%E4%BA%9B%E8%97%8F%E5%9C%A8%E7%B4%B0%E7%AF%80%E8%A3%A1%E7%9A%84%E9%AD%94%E9%AC%BC-%E4%B8%80-%E5%9F%BA%E7%A4%8E%E4%BB%8B%E7%B4%B9-dd2cd804aee1)
- [Backtracking](https://medium.com/appworks-school/%E9%80%B2%E5%85%A5%E9%81%9E%E8%BF%B4-recursion-%E7%9A%84%E4%B8%96%E7%95%8C-%E4%B8%89-d2fd70b5b171)

## Python 相關重要連結 & 筆記
- [collections.deque (used for stack & queue)](https://docs.python.org/zh-tw/3/library/collections.html#deque-objects)
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
- [Performance comparison between list & deque](https://stackoverflow.com/questions/23487307/python-deque-vs-list-performance-comparison)
- [Initialize a 2d matrix](https://www.geeksforgeeks.org/initialize-matrix-in-python/)
    ```python=
    # correct
    mat = [[0 for _ in range(cols)] for _ in range(rows)]
    mat = [[0] * cols for _ in range(rows)]
    # Wrong
    mat = [[0] * cols] * rows 
    mat = [[0 for _ in range(cols)]] * rows
    ```
- [heapq (Default: min heap)](https://docs.python.org/zh-tw/3.10/library/heapq.html)
    ```python=
    import heapq
    H = [1,3,5,7,9]
    heapq.heapify(H)
    heapq.heappush(H,2)
    _ = heapq.heappop(H)
    _ = heapq.heappushpop(H,2)    
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
- [Bit Manipulation](https://weikaiwei.com/python/python-bitwise/)
    ```python=
    >>> bin(13)
    '0b1101'
    >>> bin(200)
    '0b11001000'
    >>> int(bin(200),2)
    200
    >>> int(bin(200)[2:],2)
    200
    ```
- [bisect](https://docs.python.org/zh-tw/3/library/bisect.html)
    ```python=
    >>> import bisect
    >>> a = [1,2,3,4,5,6,7]
    >>> bisect.bisect_left(a, 4) # [1,2,3,*,4...]
    3
    >>> bisect.bisect_right(a, 4) # [1,2,3,4,*...]
    4
    >>> bisect.bisect(a, 4) # [1,2,3,4,*...]
    4    
    ```
    
    ```python=
    # binary search example
    def BinarySearch(a, x):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        else:
            return -1
    ```
- [collections.defaultdict](https://ithelp.ithome.com.tw/articles/10193094)
    ```python=
    >>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    >>> d = defaultdict(set)
    >>> for k, v in s:
    ...    d[k].add(v)
    ...
    >>> sorted(d.items())
    [('blue', {2, 4}), ('red', {1, 3})]
    ```
- collections.OrderedDict
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
- [Nonlocal vs global](https://stackoverflow.com/questions/33211272/what-is-the-difference-between-non-local-variable-and-global-variable)
- [LRU Cache](https://medium.com/@jepersyne/python-functools-lru-cache-d5cb632df710)
- A Standard Binary Search:
```python=
def binary_search(list_sorted, target):
    left, right = 0, len(list_sorted)
    while left <= right:
        mid = (left + right) // 2
        if list_sorted[mid] > target:
            right = mid - 1
        elif list_sorted[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1
