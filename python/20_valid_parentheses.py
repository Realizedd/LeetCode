from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        dic = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in dic:
                stack.append(c)
            elif not stack or dic[stack.pop()] != c:
                return False

        return not stack


