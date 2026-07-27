- [DAG and Topological Sort](https://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html)
- Kahn's Algorithm: Traverse each node with indegree = 0, and append the path 
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [-1] * numCourses
        indeg = [0] * numCourses
        order = []

        graph = defaultdict(list)
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indeg[pre[0]] += 1

        queue = deque([node for node, ids in enumerate(indeg) if ids == 0])
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []
```