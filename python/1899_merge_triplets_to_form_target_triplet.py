from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        arr = [False] * 3

        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for j in range(3):
                    arr[j] |= triplet[j] == target[j]

                if all(arr):
                    return True

        return all(arr)
