import java.util.Arrays;
import java.util.Scanner;

public class Solution {

    public int binarySearch(int[] nums, int start, int end, int target) {
        int l = start;
        int r = end;

        while (l <= r) {
            int m = l + (r - l) / 2;

            if (nums[m] == target) {
                return m;
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return -1;
    }

    public int search(int[] nums, int target) {
        int p = 0;
        int r = nums.length - 1;

        while (p < r) {
            int m = p + (r - p) / 2;

            // System.out.println("nums[p=" + p + "]: " + nums[p] + ", nums[m=" + m + "]: " + nums[m] + ", nums[r=" + r + "]: " + nums[r]);
            if (nums[p] < nums[m]) {
                p = m;
            } else {
                r = m;
            }
        }

        // System.out.println("p=" + p);

        int ans = binarySearch(nums, 0, p, target);
        return ans != -1 ? ans : binarySearch(nums, p + 1, nums.length - 1, target);
    }
    
    public static void main(String[] args) {
        int[] nums = {5,6,7,0,1,2,4};
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

         while (scanner.hasNextInt()) {
            int target = scanner.nextInt();
            System.out.println("Searching for " + target + " in " + Arrays.toString(nums) + ": " + solution.search(nums, target));
        }

        scanner.close();
    }
}