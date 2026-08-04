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
# Which to use, BFS / DFS / Backtracking?
- 第一步:問自己「這題要不要走回頭路(revisit)?」
	- **不能重複走同一格,而且要探索所有可能路徑** → Backtracking
	- **每格只走一次,找最短路徑或連通區域** → BFS / DFS(不需要 backtracking,因為不會回頭)
	這是最關鍵的分岔點。像 [[79. Word Search (M)]],同一格在**同一條路徑**裡不能重複用(所以要標記),但**換一條路徑後又要恢復原狀重新嘗試**,這種「嘗試 → 失敗就撤銷 → 換下一個可能性」的模式,就是 backtracking 的標誌。
- 第二步:如果不需要 backtracking,再問「要不要求最短距離/最少步數?」
	- **要最短路徑、最少步數、最少層數** → BFS(因為 BFS 是一層一層擴散,第一次碰到終點時保證是最短路徑)
	    - 例:迷宮最短路徑、[[994. Rotting Oranges (M)]]、[[752. Open the Lock (M)]]
	- **只要判斷連通性、找出所有連通區域、計算面積、標記訪問過的格子** → DFS 或 BFS 皆可,通常 DFS 寫起來遞迴比較簡潔
	    - 例:[[200. Number of Islands (M)]]、[[733. Flood Fill (E)]]、連通分量計算
- 題目要不要求「所有可能的解 / 路徑」?
	├─ 是 → 需要撤銷嘗試嗎(同一格在不同路徑可重複用)?
		└─ 是 → [[Backtracking]]
	└─ 否(只要判斷存在性 / 連通性 / 最短路徑)
		├─ 要最短路徑或最少步數 → [[Breadth-First Search]]
		└─ 只要連通性、面積、標記 → [[Depth-First Search]] (或 BFS,效果相同)