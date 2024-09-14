```python
class Trie:
    def __init__(self):
        self.child = {} # key: char, value: dict
        
    def insert(self, word: str) -> None:
        P = self.child
        for c in word:
            if c not in P:
                P[c] = {}
            P = P[c]
        P['end'] = True

    def search(self, word: str) -> bool:
        P = self.child
        for c in word:
            if c not in P:
                return False
            P = P[c]
        return 'end' in P

    def startsWith(self, prefix: str) -> bool:
        P = self.child
        for c in prefix:
            if c not in P:
                return False
            P = P[c]
        return True
```