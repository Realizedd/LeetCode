import java.util.Arrays;

public class Solution {

    // Sorting: O(nlog(n)) RC, O(n) SC
    public boolean isAnagramSorting(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        char[] first = s.toCharArray();
        char[] second = t.toCharArray();
        Arrays.sort(first);
        Arrays.sort(second);

        for (int i = 0; i < first.length; i++) {
            if (first[i] != second[i]) {
                return false;
            }
        }

        return true;
    }

    // Hashing: O(n) RC, O(1) SC
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] map = new int[26];

        for (int i = 0; i < s.length(); i++) {
            map[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            if (--map[s.charAt(i) - 'a'] < 0) {
                return false;
            }
        }
        
        return true;
    }
}
