class Solution:
    def index(self, char):
        return ord(char) + (-ord('A') + 26 if char.isupper() else -ord('a'))

    def contains(self, a, b):
        res = True

        for i in range(len(a)):
            if a[i] < b[i]:
                res = False
                break

        return res

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_table = [0] * (26 * 2)

        for c in t:
            t_table[self.index(c)] += 1

        min_sub = ""
        table = [0] * (26 * 2)
        left, right = 0, 0

        while right < len(s):
            if s[right] in t:
                table[self.index(s[right])] += 1

            if self.contains(table, t_table):
                min_sub = s[:(right + 1)]
                break

            right += 1
        print(t_table)
        print(table)

        if not min_sub:
            return min_sub

        while left < len(s) and right - left + 1 >= len(t):
            sub = s[left:(right + 1)]
            print(sub)
            print(table[26:])

            if self.contains(table, t_table):
                print("match:", sub)

                if len(sub) < len(min_sub):
                    min_sub = sub

                if s[left] in t:
                    print("-1 ", s[left])
                    table[self.index(s[left])] -= 1

                left += 1
            else:
                if s[left] in t:
                    print("-1 ", s[left])
                    table[self.index(s[left])] -= 1

                left += 1

                if right < len(s):
                    right += 1

                    if right < len(s) and s[right] in t:
                        print("+1 ", s[right])
                        table[self.index(s[right])] += 1

        return min_sub


sol = Solution()
print(sol.minWindow('bba', 'ab'))
