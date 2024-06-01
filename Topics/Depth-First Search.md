- Useful in various data structures ([[Tree]] / [[Graph]] / [[Matrix]])
- [[Stack]] Implementation
- Recursion Implementation

```python=
def dfs(graph, source, destination):
	N = len(graph)
	S = deque([source])
	
	visited = [False] * N
	visited[source] = True

	while S:
		current = S.pop()
		if current == destination:
			return True
			
		for neighbor in graph[current]:
			if not visited[neighbor]:
				visited[neighbor] = True # when adding to stack, marked as visited
				S.append(neighbor)

	return False

def dfs(graph, source, destination):
	N = len(graph)
	visited = [False] * N
	
	def dfs_recur(node):
		result = False
		if node == destination:
			return True
			
		for neighbor in graph[node]:
			if not visited[neighbor]:
				visited[neighbor] = True # when adding to recursion, marked as visited
				result = result or dfs_recur(neighbor)
		return result

	visited[source] = True
	return dfs(source)
```