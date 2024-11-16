- [Path](https://web.ntnu.edu.tw/~algo/Path.html)
	- Usually on a graph
	- Dijkstra's Algortihm

```python=
def dijkstra(graph, start):
    # Step 1: Initialize distances and the priority queue
    # `distance` stores the shortest path from `start` to each node
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    priority_queue = [(0, start)]  # (distance to start, node)

    while priority_queue:
        # Step 2: Extract the node with the smallest distance
        current_distance, u = heapq.heappop(priority_queue)
        
        # If this distance is already greater than the recorded one, skip
        if current_distance > distance[u]:
            continue

        # Step 3: Relax edges (update distances to neighboring nodes)
        for weight, v in graph[u]:
            new_distance = current_distance + weight
            if new_distance < distance[v]:
                # Update the distance and push the new distance to the priority queue
                distance[v] = new_distance
                heapq.heappush(priority_queue, (new_distance, v))

    return distance
```