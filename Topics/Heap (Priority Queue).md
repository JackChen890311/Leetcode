- A special kind of complete binary tree: If the value of each node in the tree is greater / less than all its child nodes, then this tree is called a max / min heap
- `H[:k]` is not top k largest / smallest!!! Use `heapq.nlargest` (not recommended due to inefficiency) or `heapq.nsmallest`, or keep popping for n times
- It's useful when you want to keep **Top K Largest / Smallest elements** as you progress traversing
- [Python heapq 介紹](https://ithelp.ithome.com.tw/articles/10247299)
- [heapq (Default: min heap)](https://docs.python.org/zh-tw/3.10/library/heapq.html)
```python=
	import heapq
	heap = [9,7,5,3,1]
	heapq.heapify(heap) # O(N)
	heapq.heappush(heap, 2)
	_ = heapq.heappop(heap)
	_ = heapq.heappushpop(heap, 2) # push -> pop
	_ = heapq.heapreplace(heap, 2) # pop -> push
	# Will not modify the heap (but inefficient)
	klargest = heapq.nlargest(k, heap)
	ksmallest = heapq.nsmallest(k, heap)
	# Use heap as priority queue
	nodes = [(5, 'A'), (2, 'B'), (9, 'C')]
	heap = []
	for node in nodes:
	    heapq.heappush(heap, (node[0], node[1])) # (priority, value)

```

| 函式                            | 順序                   | 複雜度                                                                                             | 特點                            |
| ----------------------------- | -------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------- |
| **`heapreplace(heap, item)`** | 先 **Pop** 再 **Push** | ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)O(log n) | 傳回值**一定是原本堆疊裡的元素**。若堆疊為空會噴錯。  |
| **`heappushpop(heap, item)`** | 先 **Push** 再 **Pop** | ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)O(log n) | 傳回值**可能是剛傳入的 `item`**。可用於空堆疊。 |
