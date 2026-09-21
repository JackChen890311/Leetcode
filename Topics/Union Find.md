- [[演算法] 並查集 (Union-find Algorithm)](https://ithelp.ithome.com.tw/articles/10209278)
- [Set & Disjoint Set](https://web.ntnu.edu.tw/~algo/Set.html)
- [Fucking Algorithm Union-Find](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/UnionFind%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3.md)
- [Union-Find / Disjoint-Set – 陪你刷題](https://haogroot.com/2021/01/29/union_find-leetcode/)
- Optimized code:
	- Path Compression + Union by Size / Rank
	- Time complexity: O(a(N)) ~= O(1) where a() is [inverse Ackermann function](https://zh.wikipedia.org/zh-tw/%E9%98%BF%E5%85%8B%E6%9B%BC%E5%87%BD%E6%95%B8) and can be estimated as constant for N < 10^600
	- Space complexity: O(N) for storing N elements
```python
class UF:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N
        self.count = N

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.count -= 1
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            return True # Union successful
        return False # Already in the same set

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]] # 我的老爸變成我祖父
            x = self.parent[x] # 我變成我祖父繼續找
        return x
```



