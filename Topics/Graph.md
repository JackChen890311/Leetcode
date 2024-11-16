- Representations: Adjacency Matrix / Adjacency List
	![[Pasted image 20240126151636.png]]
- [Conneted Component](https://web.ntnu.edu.tw/~algo/ConnectedComponent.html)
	- BCC, SCC, Tarjan's Algorithm, [Kosaraju's Algorithm](https://www.cnblogs.com/RioTian/p/14026585.html)
	![[Pasted image 20240128143556.png]]
-  [Why white, gray, black node during graph dfs](https://cs.stackexchange.com/questions/9676/the-purpose-of-grey-node-in-graph-depth-first-search)
	```python
	graph = ...
	N = len(graph)
	visited = [0] * N
	def dfs(node):
		if visited[node] == -1: # gray
			return False
		elif visited[node] == 1: # black
			return True
		else: # white
			visited[node] = -1
			for neighbor in graph[node]:
				if not dfs(neighbor):
					return False
			visited[node] = 1
			print(node)
			return True
	```
- [Spanning Tree](https://web.ntnu.edu.tw/~algo/SpanningTree.html)
	- Minimum Spanning [[Tree]]: A tree that connects all the nodes in a graph with minimum value / weight
		- Prim's Algorithm: starting at a node
		- Kruskal's Algorithm: starting at minimum edge
# Traversal
- 特別注意 [[Matrix]] 跟 [[Graph]] 的 traversal 比較多細節!
- [Why DFS and BFS have to put visited at different places](https://stackoverflow.com/questions/25990706/breadth-first-search-the-timing-of-checking-visitation-status/25992077#25992077)
- DFS 順序：檢查合法性與 visited 在外層 pop 出該節點後
```python=
# 初始化堆疊和已訪問集合
stack = [start_node]
visited = set()

# 開始 DFS 遍歷
while stack:
    node = stack.pop()

    # 檢查節點是否已訪問
    if node in visited:
        continue

    # 訪問這個節點 (可以在此處加入節點訪問的操作)
    print(f"Visiting: {node}")

    # 標記節點為已訪問
    visited.add(node)

    # 將所有鄰居加入堆疊
    for neighbor in graph[node]:
        if neighbor not in visited:
            stack.append(neighbor)

```
- BFS 順序：檢查合法性與 visited 的邏輯在 for loop 找鄰居裡面
```python=
from collections import deque

# 初始化隊列和已訪問集合
queue = deque([start_node])
visited = set()
visited.add(start_node)  # 起始節點標記為已訪問

# 開始 BFS 遍歷
while queue:
    node = queue.popleft()

    # 訪問這個節點 (可以在此處加入節點訪問的操作)
    print(f"Visiting: {node}")

    # 將合法且未訪問的鄰居加入隊列
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)  # 標記為已訪問
            queue.append(neighbor)  # 將鄰居加入隊列

```