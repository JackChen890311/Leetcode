- Grid-like [[Graph]]
- Moves:
	- 4-way: [(0,1), (0,-1), (1,0), (-1,0)]
	- 8-way: 4-way + [(1,1), (1,-1), (1,-1), (-1,-1)]
# Traversal
- 特別注意 [[Matrix]] 跟 [[Graph]] 的 traversal 比較多細節!
- [Why DFS and BFS have to put visited at different places](https://stackoverflow.com/questions/25990706/breadth-first-search-the-timing-of-checking-visitation-status/25992077#25992077)
- DFS 順序：檢查合法性與 visited 在外層 pop 出該節點後
```python=
# 定義方向向量 (上, 下, 左, 右)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 初始化堆疊和已訪問集合
stack = [(start_x, start_y)]
visited = set()

# 開始 DFS 遍歷
while stack:
    x, y = stack.pop()

    # 檢查單元格是否已訪問或無效
    if ((x, y) in visited) or (x not in range(rows)) or (y not in range(cols)):
        continue  # 跳過處理這個單元格

    # 訪問這個節點 (這裡可以加入訪問處理的程式碼)
    print(f"Visiting: ({x}, {y})")

    # 標記單元格為已訪問
    visited.add((x, y))

    # 處理鄰居
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        stack.append((nx, ny))  # 將鄰居加入堆疊
```
- BFS 順序：檢查合法性與 visited 的邏輯在 for loop 找鄰居裡面
```python=
# 定義方向向量 (上, 下, 左, 右)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 初始化隊列和已訪問集合
queue = deque([(start_x, start_y)])
visited = set()
visited.add((start_x, start_y))  # 起始點標記為已訪問

# 開始 BFS 遍歷
while queue:
    x, y = queue.popleft()  # 使用 popleft 取出隊首元素進行處理

    # 訪問這個節點 (這裡可以加入訪問處理的程式碼)
    print(f"Visiting: ({x}, {y})")

    # 處理鄰居
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 先檢查鄰居是否合法且未訪問
        if (nx, ny) not in visited and (nx in range(rows)) and (ny in range(cols)):
            visited.add((nx, ny))  # 標記為訪問過
            queue.append((nx, ny))  # 加入到隊列中等待處理
```