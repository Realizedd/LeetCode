public class Solution {

    public int removeDuplicates(int[] nums) {
        if (nums.length <= 1) {
            return nums.length;
        }

        int duplicates = 0;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                duplicates++;
            }

            nums[i - duplicates] = nums[i];
        }

        return nums.length - duplicates;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,2,3,3,4,5,6,7,7,7,8,9};
        Solution solution = new Solution();
        int k = solution.removeDuplicates(nums);
        for (int i = 0; i < k; i++) {
            System.out.println(nums[i]);
        }
    }
}