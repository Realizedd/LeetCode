class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = {}

        def count(cur_goal, unique):
            if cur_goal == 0 and unique == 0:
                return 1
            if cur_goal == 0 or unique == 0 and cur_goal != unique:
                return 0
            if (cur_goal, unique) in dp:
                return dp[(cur_goal, unique)]

            dp[(cur_goal, unique)] = count(cur_goal - 1, unique - 1) * (n - unique + 1)

            if unique > k:
                dp[(cur_goal, unique)] += count(cur_goal - 1, unique) * (unique - k)

            return dp[(cur_goal, unique)] % (10 ** 9 + 7)

        return count(goal, n)


