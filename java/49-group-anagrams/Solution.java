import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    private static boolean equals(int[] a, int[] b) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }

        return true;
    }

    private class Occurrences {

        private int[] occurrences = new int[26];

        Occurrences(char[] arr) {
            for (char c : arr) {
                occurrences[c - 'a']++;
            }
        }

        @Override
        public boolean equals(Object obj) {
            if (!(obj instanceof Occurrences)) {
                return false;
            }

            return obj == this || Solution.equals(occurrences, ((Occurrences) obj).occurrences);
        }

        @Override
        public int hashCode() {
            return Arrays.hashCode(occurrences);
        }
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Occurrences, List<String>> occurrences = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            List<String> list = occurrences.computeIfAbsent(new Occurrences(strs[i].toCharArray()), res -> new ArrayList<>());
            list.add(strs[i]);
        }

        List<List<String>> ans = new ArrayList<>();
        ans.addAll(occurrences.values());
        return ans;
    }

    public static void main(String[] args) {
        String[] strs = { "hhhhu", "tttti", "tttit", "hhhuh", "hhuhh", "tittt" };
        Solution solution = new Solution();
        System.out.println(solution.groupAnagrams(strs));
    }
}
