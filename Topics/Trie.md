```python
class Trie:
    def __init__(self):
        def inf_ddict():
            return defaultdict(inf_ddict)
        self.child = inf_ddict() # key: char, value: dict
        
    def insert(self, word: str) -> None:
        P = self.child
        for c in word:
            P = P[c]
        P['end'] = True
    
    def _searchTool(self, word: str) -> bool:
        P = self.child
        for c in word:
            if c not in P:
                return False
            P = P[c]
        return P

    def search(self, word: str) -> bool:
        result = self._searchTool(word)
        return 'end' in result if result else False

    def startsWith(self, prefix: str) -> bool:
        result = self._searchTool(prefix)
        return True if result else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```