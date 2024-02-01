- A special kind of complete binary tree
- [Python heapq 介紹](https://ithelp.ithome.com.tw/articles/10247299)
- [heapq (Default: min heap)](https://docs.python.org/zh-tw/3.10/library/heapq.html)
    ```python=
    import heapq
    H = [1,3,5,7,9]
    heapq.heapify(H)
    heapq.heappush(H,2)
    _ = heapq.heappop(H)
    _ = heapq.heappushpop(H,2)    
    ```