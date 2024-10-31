- Use recursive default dict
- When inserting a word, use `curr = curr[c] for c in word`, also add a `END` when finish
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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```