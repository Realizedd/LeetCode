import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    continue;
                }

                Map<Integer, Integer> list = map.computeIfAbsent(nums[i] + nums[j], result -> new HashMap<>());

                if (!list.containsKey(i) && !list.containsKey(j)) {
                    list.put(i, j);
                }
            }
        }

        Map<Integer, Map<Integer, Integer>> sums = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            System.out.println("i: " + i + ", nums[i]: " + nums[i]);
            Map<Integer, Integer> inverse = map.get(-nums[i]);

            if (inverse != null) {
                for (Map.Entry<Integer, Integer> entry : inverse.entrySet()) {
                    System.out.println("<" + nums[entry.getKey()] + ", " + nums[entry.getValue()] + "> (" + entry.getKey() + ", " + entry.getValue() + ")");
                    if (entry.getKey().intValue() != i && entry.getValue().intValue() != i) {
                        Map<Integer, Integer> list = sums.computeIfAbsent(nums[i], result -> new HashMap<>());

                        if (!list.containsKey(nums[entry.getKey()]) && !list.containsKey(nums[entry.getValue()])) {
                            list.put(nums[entry.getKey()], nums[entry.getValue()]);
                        }
                    }
                }
            }

            System.out.println();
        }

        for (Map.Entry<Integer, Map<Integer, Integer>> entry : sums.entrySet()) {
            for (Map.Entry<Integer, Integer> sum : entry.getValue().entrySet()) {       
                List<Integer> answer = new ArrayList<>();
                answer.add(sum.getKey());
                answer.add(sum.getValue());
                answer.add(entry.getKey());
                ans.add(answer);
            }
        }
        
        return ans;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-1,0,1,2,-1,-4};
        System.out.println(solution.threeSum(nums));
    }
}