import java.util.Arrays;

public class Solution {

    public void reverse(int[] arr, int start) {
        for (int i = 0; i < (arr.length - start) / 2; i++) {
            int temp = arr[i + start];
            arr[i + start] = arr[arr.length - i - 1];
            arr[arr.length - i + - 1] = temp;
        }
    }

    public void nextPermutation(int[] nums) {
        int incrIndex = 0;

        for (int i = nums.length - 1; i > 0; i--) {
            if (nums[i - 1] < nums[i]) {
                incrIndex = i;
                break;
            }
        }

        // System.out.println("incrIndex=" + incrIndex + " (val=" + nums[incrIndex] + ")");
        // System.out.println(Arrays.toString(nums));

        if (incrIndex > 0) {
            int targetIndex = incrIndex - 1;
            int n = nums[targetIndex];
            int next = -1;

            for (int j = targetIndex + 1; j < nums.length; j++) {
                if (nums[j] > n) {
                    if (next == -1) {
                        next = j;
                    } else if (nums[j] <= nums[next]) {
                        next = j;
                    }
                }
            }

            // System.out.println("next=" + next + " (val=" + (next != -1 ? nums[next] : "none") + ")");

            if (next != -1) {
                int temp = nums[targetIndex];
                nums[targetIndex] = nums[next];
                nums[next] = temp;
            }
        }
        
        // System.out.println(Arrays.toString(nums));
        reverse(nums, incrIndex);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {2,3,1,3,3};
        System.out.println(Arrays.toString(nums));
        solution.nextPermutation(nums);
        System.out.println(" --> " + Arrays.toString(nums));
    }
 }