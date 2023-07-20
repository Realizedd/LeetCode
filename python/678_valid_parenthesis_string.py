class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1

            if leftMax < 0:
                return False

            if leftMin < 0:
                leftMin = 0

        return leftMin == 0

    def checkValidStringDP(self, s: str) -> bool:
        dp = {}

        def dfs(idx, cnt):
            if cnt < 0:
                return False
            if idx == len(s):
                return cnt == 0
            if (idx, cnt) in dp:
                return dp[(idx, cnt)]

            c = s[idx]

            if c == ')':
                dp[(idx, cnt)] = dfs(idx + 1, cnt - 1) if cnt > 0 else False
            elif c == '*':
                dp[(idx, cnt)] = dfs(idx + 1, cnt + 1) | dfs(idx + 1, cnt - 1) | dfs(idx + 1, cnt)
            else:
                dp[(idx, cnt)] = dfs(idx + 1, cnt + 1)

            return dp[(idx, cnt)]

        return dfs(0, 0)
