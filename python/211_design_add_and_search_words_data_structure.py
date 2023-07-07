class WordDictionary:

    def __init__(self):
        self.head = TrieNode('')

    def addWord(self, word: str) -> None:
        prev = None
        cur = self.head

        for c in word:
            prev = cur
            cur = prev.map.get(c, TrieNode(c))
            prev.map[c] = cur

        cur.end = True

    def search(self, word: str) -> bool:
        def recurSearch(node, idx):
            if idx == len(word):
                return node.end

            char = word[idx]
            targets = []

            if char == '.':
                targets += node.map.values()
            else:
                if char not in node.map:
                    return False

                targets.append(node.map[char])

            for target in targets:
                if recurSearch(target, idx + 1):
                    return True

            return False

        return recurSearch(self.head, 0)


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.map = {}
        self.end = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)