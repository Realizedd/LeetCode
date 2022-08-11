public class Solution {

    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int neg = 0;
        int zeros = 0;
        int zeroIndex = -1;
        int prod = 1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                zeros++;
                zeroIndex = i;
                continue;
            }

            if (nums[i] < 0) {
                neg++;
            }

            prod *= Math.abs(nums[i]);
        }

        if (zeros > 1) {
            return ans;
        } else if (zeros == 1) {
            ans[zeroIndex] = (neg % 2 == 0 ? 1 : -1) * prod;
            return ans;
        }

        for (int i = 0; i < nums.length; i++) {
            int negs = nums[i] > 0 ? neg : (neg - 1);
            ans[i] = (negs % 2 == 0 ? 1 : -1) * (prod / Math.abs(nums[i]));
        }

        return ans;
    }
}
