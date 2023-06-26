public class Solution {

    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        boolean hasZero = false;
        int zeroIndex = -1;
        int nonZeroProd = 1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                if (hasZero) {
                    return ans;
                }
                
                hasZero = true;
                zeroIndex = i;
                continue;
            }

            nonZeroProd *= nums[i];
        }

        if (hasZero) {
            ans[zeroIndex] = nonZeroProd;
            return ans;
        }

        for (int i = 0; i < nums.length; i++) {
            ans[i] = nonZeroProd / nums[i];
        }

        return ans;
    }
}
