import java.util.Arrays;

public class Solution {

    public void nextPermutation(int[] nums) {
        for (int i = nums.length - 1; i > 0; i--) {
            if (nums[i] <= nums[i - 1]) {
                continue;
            }

            int n = nums[i - 1];
            int next = -1;

            for (int j = i; j < nums.length - 1; j++) {
                if (nums[j] > n) {
                    if (next == -1) {
                        next = j;
                    } else if (nums[j] < nums[next]) {
                        next = j;
                    }
                }
            }

            if (next != -1) {
                int temp = nums[next];
                nums[next] = nums[i - 1];
                nums[i - 1] = temp;
                break;
            }

            System.out.println("n=" + n + ", next=" + (next != -1 ? nums[next] : "none"));
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1,2,3};
        System.out.println(Arrays.toString(nums));
        solution.nextPermutation(nums);
        System.out.println(Arrays.toString(nums));
    }
 }