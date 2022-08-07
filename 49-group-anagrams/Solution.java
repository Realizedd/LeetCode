import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    public static int compare(int[] a, int[] b) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return a[i] - b[i];
            }
        }

        return 0;
    }

    private class StringWrapper implements Comparable<StringWrapper> {

        private String[] strs;
        private int index;
        private int[] occurrences = new int[26];

        StringWrapper(String[] strs, int index) {
            this.strs = strs;
            this.index = index;

            for (char c : strs[index].toCharArray()) {
                occurrences[c - 'a']++;
            }
        }

        @Override
        public int compareTo(StringWrapper other) {
            int value = Integer.compare(toString().length(), other.toString().length());
            return value == 0 ? Solution.compare(occurrences, other.occurrences) : value;
        }

        @Override
        public String toString() {
            return strs[index];
        }
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        StringWrapper[] arr = new StringWrapper[strs.length];

        for (int i = 0; i < strs.length; i++) {
            arr[i] = new StringWrapper(strs, i);
        }

        Arrays.sort(arr);

        List<List<String>> ans = new ArrayList<>();
        StringWrapper prev = null;
        List<String> answer = null;

        for (StringWrapper wrapper : arr) {
            if (prev == null || prev.compareTo(wrapper) != 0) {
                ans.add(answer = new ArrayList<>());
            }

            answer.add(wrapper.toString());
            prev = wrapper;
        }

        return ans;
    }

    public static void main(String[] args) {
        String[] strs = { "hhhhu", "tttti", "tttit", "hhhuh", "hhuhh", "tittt" };
        Solution solution = new Solution();
        System.out.println(solution.groupAnagrams(strs));
    }
}
