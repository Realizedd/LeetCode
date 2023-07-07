class Trie:

    def __init__(self):
        self.head = TrieNode('')

    def insert(self, word: str) -> None:
        prev = None
        cur = self.head

        for c in word:
            prev = cur
            cur = prev.map.get(c, TrieNode(c))
            prev.map[c] = cur

        cur.map['*'] = TrieNode('')

    def search(self, word: str) -> bool:
        cur = self.head

        for c in word:
            if c not in cur.map:
                return False

            cur = cur.map[c]

        return '*' in cur.map

    def startsWith(self, prefix: str) -> bool:
        cur = self.head

        for c in prefix:
            if c not in cur.map:
                return False

            cur = cur.map[c]

        return True


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.map = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)