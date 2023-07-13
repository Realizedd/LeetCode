from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        visited = set()
        queue = deque()
        changes = 1
        queue.append(beginWord)
        visited.add(beginWord)

        while queue:
            for i in range(len(queue)):
                s = queue.popleft()

                if s == endWord:
                    return changes

                for j in range(len(s)):
                    pre, suf = s[:j], s[(j+1):]

                    for a in range(26):
                        word = pre + chr(ord('a') + a) + suf

                        if word in wordList and word not in visited:
                            queue.append(word)
                            visited.add(word)

            changes += 1

        return 0


sol = Solution()
print(sol.ladderLength('qa', 'sq', ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))