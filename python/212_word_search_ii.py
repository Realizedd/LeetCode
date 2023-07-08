from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()

        for word in words:
            trie.addWord(word)

        res = []

        def dfs(r, c, node, word):
            if board[r][c] not in node.neighbors:
                return

            temp = board[r][c]
            node = node.neighbors[temp]

            if node.end:
                node.end = False
                res.append(word + node.char)

            board[r][c] = '#'

            if r + 1 < m:
                dfs(r + 1, c, node, word + temp)

            if c + 1 < n:
                dfs(r, c + 1, node, word + temp)

            if r - 1 >= 0:
                dfs(r - 1, c, node, word + temp)

            if c - 1 >= 0:
                dfs(r, c - 1, node, word + temp)

            board[r][c] = temp

        for row in range(m):
            for col in range(n):
                dfs(row, col, trie.head, "")

        return res


class Trie:
    def __init__(self):
        self.head = TrieNode('')

    def addWord(self, word):
        cur = self.head

        for c in word:
            if c not in cur.neighbors:
                cur.neighbors[c] = TrieNode(c)

            cur = cur.neighbors[c]

        cur.end = True


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.neighbors = {}
        self.end = False
