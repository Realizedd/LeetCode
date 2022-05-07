import java.util.Arrays;

public class Solution {

    public int[] searchRange(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int min = -1;
        
        while (l <= r) {
            int m = l + (r - l) / 2;

            if (nums[m] == target) {
                if (m - 1 >= 0 && nums[m - 1] == target) {
                    r = m - 1;
                } else {
                    min = m;
                    break;
                }
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        l = 0;
        r = nums.length - 1;
        int max = -1;
        
        while (l <= r) {
            int m = l + (r - l) / 2;

            if (nums[m] == target) {
                if (m + 1 <= nums.length - 1 && nums[m + 1] == target) {
                    l = m + 1;
                } else {
                    max = m;
                    break;
                }
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        // System.out.println("min=" + min + ", nums[min]=" + nums[min] + ", max=" + max + ", nums[max]=" + nums[max]);

        return new int[] {min, max};
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {3,4,4,4,5,6,7,7,7,8,8,8,8,9,9,10};
        int target = 5;
        System.out.println("Searching for " + target + " in " + Arrays.toString(nums) + ": " + Arrays.toString(solution.searchRange(nums, target)));
    }
}
