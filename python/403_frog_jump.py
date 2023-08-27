from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_pos = set(stones)
        dp = {}

        def jump(last_jump, pos):
            if pos not in stone_pos:
                return False
            if (last_jump, pos) in dp:
                return dp[(last_jump, pos)]
            if pos == stones[len(stones) - 1]:
                return True

            res = False

            if last_jump > 1:
                res |= jump(last_jump - 1, pos + last_jump - 1)

            if last_jump > 0:
                res |= jump(last_jump, pos + last_jump)

            dp[(last_jump, pos)] = res | jump(last_jump + 1, pos + last_jump + 1)
            return dp[(last_jump, pos)]

        return jump(-1, 0)