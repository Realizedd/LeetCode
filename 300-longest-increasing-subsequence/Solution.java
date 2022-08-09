public class Solution {

    public int recLen(int[] nums, int index, int last, int seq) {
        if (index == nums.length - 1) {
            return seq;
        }

        int cur = nums[last];
        int next = nums[index + 1];

        if (next > cur) {
            return Math.max(recLen(nums, index + 1, index, seq), recLen(nums, index + 1, index, seq + 1));
        } else {
            return recLen(nums, index + 1, last, seq);
        }
    }

    public int lengthOfLIS(int[] nums) {
        int max = 0;

        for (int i = 0; i < nums.length; i++) {
            Math.max(max, recLen(nums, i, i, 1));
        }

        return max;
    }
}
