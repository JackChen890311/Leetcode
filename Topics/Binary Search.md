- [Binary search](https://medium.com/appworks-school/binary-search-%E9%82%A3%E4%BA%9B%E8%97%8F%E5%9C%A8%E7%B4%B0%E7%AF%80%E8%A3%A1%E7%9A%84%E9%AD%94%E9%AC%BC-%E4%B8%80-%E5%9F%BA%E7%A4%8E%E4%BB%8B%E7%B4%B9-dd2cd804aee1)
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
    >>> bisect.insort(a, 8) # insert element
    >>> a
    [1,2,3,4,5,6,7,8]
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
- A Standard Binary Search:
```python=
def binary_search(list_sorted, target):
    left, right = 0, len(list_sorted) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if list_sorted[mid] > target:
            right = mid - 1
        elif list_sorted[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1