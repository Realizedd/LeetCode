import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answers = new ArrayList<>();

        if (nums.length < 3) {
            return answers;
        }
        
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int low = i + 1;
            int high = nums.length - 1;
            int sum = -nums[i];

            while (low < high) {
                if (nums[low] + nums[high] == sum) {
                    answers.add(Arrays.asList(nums[i], nums[low], nums[high]));

                    while (low < high && nums[low] == nums[low + 1]) {
                        low++;
                    }

                    while (low < high && nums[high] == nums[high - 1]) {
                        high--;
                    }

                    low++; 
                    high--;
                } else if (nums[low] + nums[high] < sum) {
                    low++;
                } else {
                    high--;
                }
            }
        }

        return answers;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-1,0,1,2,2,2,2,2,-1,-4};
        System.out.println(solution.threeSum(nums));
    }
}