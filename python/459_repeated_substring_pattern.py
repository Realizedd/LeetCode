class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for window in range(n // 2, 0, -1):
            if n % window != 0:
                continue

            segment = s[:window]
            res = True

            for i in range(1, n // window):
                start = i * window

                if s[start:(start + window)] != segment:
                    res = False
                    break

            if res:
                return True

        return False

    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s

        if s in t[1:-1]:
            return True

        return False
