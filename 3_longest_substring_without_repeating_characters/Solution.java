import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {

    public int lengthOfLongestSubstring(String s) {
        int len = s.length();

        if (len == 0) {
            return 0;
        }

        Map<Character, Integer> used = new HashMap<>(256);
        int record = 0;
        int count = 0;

        for (int i = 0; i < len; i++) {
            Character c = s.charAt(i);

            // Found a duplicate key. Return to the other matching key's position + 1 and check for substring again
            if (used.containsKey(c)) {
                count = 0;
                i = used.get(c);
                used.clear();
                continue; // Auto-increment to used.get(c) + 1
            }

            count++;
            record = Math.max(count, record);
            used.put(c, i);
        }

        return record;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            System.out.println(in + ": " + solution.lengthOfLongestSubstring(in));
        }
        scanner.close();
    }
}