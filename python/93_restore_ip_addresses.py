from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        ans = []

        def generate(idx, k, cur):
            if idx >= len(s):
                if k == 0:
                    ans.append('.'.join(cur))
                return
            if k == 0:
                return

            cur.append(s[idx])
            generate(idx + 1, k - 1, cur)
            cur.pop()

            if s[idx] == '0' or idx + 1 >= len(s):
                return

            cur.append(s[idx:idx + 2])
            generate(idx + 2, k - 1, cur)
            cur.pop()

            val = s[idx:idx + 3]

            if int(val) > 255 or idx + 2 >= len(s):
                return

            cur.append(s[idx:idx + 3])
            generate(idx + 3, k - 1, cur)
            cur.pop()

        generate(0, 4, [])
        return ans


sol = Solution()
print(sol.restoreIpAddresses('25525511135'))