class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1) + len(num2)
        ans = [0] * n

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                res = int(num1[i]) * int(num2[j])
                ans[1 + (i + j)] += res

        carry = 0
        print(ans)

        for i in range(n - 1, -1, -1):
            total = carry + ans[i]
            print(i, total)

            if total > 9:
                carry = total // 10
            else:
                carry = 0

            ans[i] = total % 10

        ans = ans if ans[0] else ans[1:]
        return ''.join([str(n) for n in ans])


sol = Solution()
print(sol.multiply(num1 = "9999", num2 = "9999"))