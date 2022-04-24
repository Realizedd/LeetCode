import java.util.Arrays;

public class Solution {

    public int threeSumClosest(int[] nums, int target) {
        int closest = nums[0] + nums[1] + nums[2];
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int low = i + 1;
            int high = nums.length - 1;

            while (low < high) {
                int sum = nums[low] + nums[high] + nums[i];
                
                if (sum == target) {
                    return target;
                } else if (sum < target) {
                    if (Math.abs(target - sum) < Math.abs(target - closest)) {
                        closest = sum;
                    }

                    low++;
                } else {
                    if (Math.abs(target - sum) < Math.abs(target - closest)) {
                        closest = sum;
                    }

                    high--;
                }
            }
        }

        return closest;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-1,0,1,2,2,2,2,2,-1,-4};
        System.out.println(solution.threeSumClosest(nums, 19));
    }
}