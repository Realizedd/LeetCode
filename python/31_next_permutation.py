from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        rev_inc_idx = n - 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break

            rev_inc_idx = i

        if rev_inc_idx > 0:
            j = n - 1

            while nums[j] <= nums[rev_inc_idx - 1]:
                j -= 1

            nums[rev_inc_idx - 1], nums[j] = nums[j], nums[rev_inc_idx - 1]

        nums[rev_inc_idx:n] = reversed(nums[rev_inc_idx:n])


sol = Solution()
res = [1,2,3,4,5]

for _ in range(120):
    print(res)
    sol.nextPermutation(res)