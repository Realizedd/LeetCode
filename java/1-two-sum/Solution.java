import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {

    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];

            if (map.containsKey(target - val)) {
                ans[0] = i;
                ans[1] = map.get(target - val);
                return ans;
            } else {
                map.put(val, i);
            }
        }

        return ans;
    }   

    public int[] twoSumBruteForce(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; i < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }    
        }

        return new int[] {-1, -1};
    }

    public static void main(String[] args) {
        int[] arr = {3,2,4};
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.twoSum(arr, 6)));
    }
}
