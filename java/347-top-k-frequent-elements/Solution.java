import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Solution {

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        TreeMap<Integer, List<Integer>> treeMap = new TreeMap<>();

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            List<Integer> list = treeMap.computeIfAbsent(entry.getValue(), res -> new LinkedList<>());
            list.add(entry.getKey());
        }

        int[] ans = new int[k];
        int i = 0;
        Map.Entry<Integer, List<Integer>> entry = treeMap.pollLastEntry();

        while (i < k) {
            LinkedList<Integer> list = (LinkedList<Integer>) entry.getValue();
            ans[i++] = list.poll();

            if (list.isEmpty()) {
                entry = treeMap.pollLastEntry();
            }
        }

        return ans;
    }
}
