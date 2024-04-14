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