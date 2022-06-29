public class Solution {

    public int makeJump(int[] nums, int index, int jump, int jumps) {
        if (index + jump > nums.length - 1) {
            return 0;
        } else if (index + jump == nums.length - 1) {
            return jumps + 1;
        } else {
            return makeJump(nums, index + jump, nums[index], jumps + 1);
        }
    }

    public int jump(int[] nums) {
        
    }
}