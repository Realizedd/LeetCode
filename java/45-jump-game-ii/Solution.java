public class Solution {

    // READ: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/506853/Java-A-general-greedy-solution-to-process-similar-problems

    public int makeJump(int[] nums, int index, int jumps) {
        if (index == nums.length - 1) {
            System.out.println(jumps);
            return jumps;
        }

        int maxJump = nums[index];

        if (index + maxJump >= nums.length) {
            maxJump = nums.length - 1 - index;
        }

        int jumpsCount = makeJump(nums, index + maxJump, jumps + 1);

        for (int jump = maxJump - 1; jump >= 0; jump--) {
            jumpsCount = makeJump(nums, index + jump, jumps + 1);
        }

        return jumpsCount;
    }

    public int jump(int[] nums) {
        return makeJump(nums, 0, 0);
    }
}