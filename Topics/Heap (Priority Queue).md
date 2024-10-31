- A special kind of complete binary tree: If the value of each node in the tree is greater / less than all its child nodes, then this tree is called a max / min heap
- `H[:k]` is not top k largest / smallest!!! Use `heapq.nlargest` (not recommended due to inefficiency) or `heapq.nsmallest`
- It's useful when you want to keep **Top K Largest / Smallest elements** as you progress traversing
- [Python heapq 介紹](https://ithelp.ithome.com.tw/articles/10247299)
- [heapq (Default: min heap)](https://docs.python.org/zh-tw/3.10/library/heapq.html)

    ```python=
    import heapq
    H = [1,3,5,7,9]
    heapq.heapify(H)
    heapq.heappush(H,2)
    _ = heapq.heappop(H)
    _ = heapq.heappushpop(H,2)
    klargest = heapq.nlargest(k, H)
    ksmallest = heapq.nsmallest(k, H)
    ```