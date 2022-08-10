public class Solution {

    public int recLen(int[] nums, int[] ans, int index, int last, int seq) {
        if (ans[index] >= 0) {
            return seq + ans[index];
        }

        if (index == nums.length - 1) {
            return seq;
        }

        int cur = nums[last];
        int next = nums[index + 1];

        if (next > cur) {
            return Math.max(recLen(nums, ans, index + 1, index + 1, seq + 1), recLen(nums, ans, index + 1, last, seq));
        } else {
            return recLen(nums, ans, index + 1, last, seq);
        }
    }

    public int lengthOfLIS(int[] nums) {
        int[] ans = new int[nums.length];

        for (int i = 0; i < ans.length; i++) {
            ans[i] = -1;
        }

        int max = 0;

        for (int i = 0; i < nums.length; i++) {
            ans[i] = recLen(nums, ans, i, i, 1);
            max = Math.max(max, ans[i]);
        }

        return max;
    }

    public static void main(String[] args) {
        int[] arr = new int[50];

        for (int i = 1; i <= 50; i++) {
            arr[i - 1] = i;
        }

        Solution solution = new Solution();
        System.out.println(solution.lengthOfLIS(arr));
    }
}
