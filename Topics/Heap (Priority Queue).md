- A special kind of complete binary tree: If the value of each node in the tree is greater / less than all its child nodes, then this tree is called a max / min heap
- `H[:k]` is not top k largest / smallest!!! Use `heapq.nlargest` (not recommended due to inefficiency) or `heapq.nsmallest`, or keep popping for n times
- It's useful when you want to keep **Top K Largest / Smallest elements** as you progress traversing
- [Python heapq 介紹](https://ithelp.ithome.com.tw/articles/10247299)
- [heapq (Default: min heap)](https://docs.python.org/zh-tw/3.10/library/heapq.html)
```python=
	import heapq
	heap = [9,7,5,3,1]
	heapq.heapify(heap)
	heapq.heappush(heap, 2)
	_ = heapq.heappop(heap)
	_ = heapq.heappushpop(heap, 2)
	# Will not modify the heap (but inefficient)
	klargest = heapq.nlargest(k, heap)
	ksmallest = heapq.nsmallest(k, heap)
	# Use heap as priority queue
	nodes = [(5, 'A'), (2, 'B'), (9, 'C')]
	heap = []
	for node in nodes:
	    heapq.heappush(heap, (node[0], node[1])) # (priority, value)
```