from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        words.append('')
        ans = []
        cur = []
        size = 0

        for i, word in enumerate(words):
            if size + len(cur) + len(word) <= maxWidth and i < n:
                cur.append(word)
                size += len(word)
            else:
                spaces = maxWidth - size
                numWords = max(len(cur) - 1, 1)
                width = (spaces // numWords) if i < n else 1
                remainder = (spaces % numWords) if i < n else 0
                line = ''

                for j in range(len(cur)):
                    w = cur[j]
                    line += w

                    if j < len(cur) - 1:
                        line += (' ' * width)
                        spaces -= width

                        if remainder > 0:
                            line += ' '
                            remainder -= 1
                            spaces -= 1

                    elif spaces > 0:
                        line += (' ' * spaces)

                ans.append(line)

                cur = [word]
                size = len(word)

        return ans
