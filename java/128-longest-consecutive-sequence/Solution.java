import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Solution {

    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], 1);
        }

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i] - 1)) {
                int sum = map.get(nums[i]) + map.get(nums[i] - 1);
                map.put(nums[i], sum);
                map.put(nums[i] - 1, sum);
            }
        }

        int max = 0;

        for (int n : map.values()) {
            max = Math.max(max, n);
        }

        return max;
    }

    public static void main(String[] args) {
        int[] arr = { 0, 100, 4, 200, 1, 3, 2};
        Solution solution = new Solution();
        List<Integer> list = new ArrayList<>();
        Set<Integer> set = new HashSet<>();
        for (int n : arr) {
            set.add(n);
        }
        list.addAll(set);
        Collections.sort(list);
        System.out.println(list);
        System.out.println(solution.longestConsecutive(arr));
    }
}
