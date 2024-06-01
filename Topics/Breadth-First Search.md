- Useful in various data structures ([[Tree]] / [[Graph]] / [[Matrix]])
- [[Queue]] Implementation
- Recursion Implementation (Less common)

```python=
def bfs(graph, source, destination):
	N = len(graph)
	Q = deque([source])
	
	visited = [False] * N
	visited[source] = True

	while Q:
		current = Q.popleft()
		if current == destination:
			return True
			
		for neighbor in graph[current]:
			if not visited[neighbor]:
				visited[neighbor] = True # when adding to queue, marked as visited
				Q.append(neighbor)

	return False

```