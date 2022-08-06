import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class Solution {
    
    private boolean equals(int[] a, int[] b) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }

        return true;
    }
    
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Integer, List<Integer>> sameLengths = new HashMap<>();
        int[][] map = new int[strs.length][26];

        for (int i = 0; i < strs.length; i++) {
            String s = strs[i];
            List<Integer> list = sameLengths.computeIfAbsent(s.length(), res -> new ArrayList<>());
            list.add(i);

            for (int j = 0; j < s.length(); j++) {
                map[i][s.charAt(j) - 'a']++;
            }
        }

        List<List<String>> ans = new ArrayList<>();

        for (int i = 0; i < strs.length; i++) {
            List<String> answer = new ArrayList<>();
            String s = strs[i];

            List<Integer> list = sameLengths.get(s.length());
            Iterator<Integer> iterator = list.iterator();

            while (iterator.hasNext()) {
                int j = iterator.next();

                if (i == j || equals(map[i], map[j])) {
                    answer.add(strs[j]);
                    iterator.remove();
                }
            }

            if (answer.isEmpty()) {
                continue;
            }

            ans.add(answer);
        }

        return ans;
    }
}
