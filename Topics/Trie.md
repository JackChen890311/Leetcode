- Use recursive default dict
- When inserting a word, use `curr = curr[c] for c in word`, also add a `END` when finish
- [[208. Implement Trie (Prefix Tree) (M)]]:
```python
class Trie:
    def __init__(self):
        nested_ddict = lambda: defaultdict(nested_ddict)
        self.tree = nested_ddict()

    def insert(self, word: str) -> None:
        curr_tree = self.tree
        for c in word:
            curr_tree = curr_tree[c]
        curr_tree['END'] = ''

    def _search_tool(self, dest: str) -> tuple[bool, defaultdict]:
        curr_tree = self.tree
        for c in dest:
            if c not in curr_tree:
                return False, defaultdict()
            curr_tree = curr_tree[c]
        return True, curr_tree

    def search(self, word: str) -> bool:
        status, curr_tree = self._search_tool(word)
        if not status:
            return False
        return True if 'END' in curr_tree else False

    def startsWith(self, prefix: str) -> bool:
        status, curr_tree = self._search_tool(prefix)
        return status
```
-  Or using a self-defined trie node
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```