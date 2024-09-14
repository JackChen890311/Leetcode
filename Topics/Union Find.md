- [[演算法] 並查集 (Union-find Algorithm)](https://ithelp.ithome.com.tw/articles/10209278)
- [Set & Disjoint Set](https://web.ntnu.edu.tw/~algo/Set.html)
- [Fucking Algorithm Union-Find](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/UnionFind%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3.md)
- [Union-Find / Disjoint-Set – 陪你刷題](https://haogroot.com/2021/01/29/union_find-leetcode/)
- Optimized code:
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

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
```