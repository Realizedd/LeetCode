import java.util.Arrays;

public class Solution {

    // NOT MY SOLUTION - https://leetcode.com/problems/first-missing-positive/discuss/17214/Java-simple-solution-with-documentation
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (nums[i] <= 0 || nums[i] > n) {
                nums[i] = n + 1;
            }
        }

        System.out.println(Arrays.toString(nums));

        for (int i = 0; i < n; i++) {
            int num = Math.abs(nums[i]);

            if (num > n) {
                continue;
            }

            num--;
            
            if (nums[num] > 0) {
                nums[num] = -1 * nums[num];
            }
        }

        System.out.println(Arrays.toString(nums));

        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                return i + 1;
            }
        }

        return n + 1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.firstMissingPositive(new int[] {1,2,0}));
        System.out.println(solution.firstMissingPositive(new int[] {3,4,-1,1}));
        System.out.println(solution.firstMissingPositive(new int[] {7,8,9,10,11,12}));
    }
}
