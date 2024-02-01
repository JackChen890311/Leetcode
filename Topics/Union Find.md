- [[演算法] 並查集 (Union-find Algorithm)](https://ithelp.ithome.com.tw/articles/10209278)
- [Set & Disjoint Set](https://web.ntnu.edu.tw/~algo/Set.html)
- [Fucking Algorithm Union-Find](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/UnionFind%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3.md)
- Code:
```python
class UF:
    def __init__(self,N):
        self.parent = list(range(N))
        self.count = N

    def union(self, x, y):
	    if self.find(x) != self.find(y):
	        self.parent[self.find(x)] = self.find(y)
	        self.count -= 1

    def find(self, x):
        final = x
        while self.parent[final] != final:
            final = self.parent[final]

        while self.parent[x] != final:
            origin = self.parent[x]
            self.parent[x] = final
            x = origin
        return final
        
```