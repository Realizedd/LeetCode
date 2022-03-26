import java.util.Scanner;

public class Solution {

    private boolean isPalindrome(String s, int start, int end) {
        int len = end - start + 1;
        
        for (int i = 0; i < len / 2; i++) {
            if (s.charAt(start + i) != s.charAt(end - i)) {
                return false;
            }
        }

        return true;
    }

    // Brute Force Method: RC O(n^3), SC O(1)
    public String longestPalindrome(String s) {
        int len = s.length();

        if (len <= 1) {
            return s;
        }

        String longest = s.charAt(0) + "";
        boolean found = false;

        for (int groupLen = len; groupLen >= 2; groupLen--) {

            for (int start = 0; start < len - groupLen + 1; start++) {
                int end = start + groupLen - 1;

                if (isPalindrome(s, start, end)) {
                    longest = s.substring(start, end + 1);
                    found = true;
                    break;
                }
            }

            if (found) {
                break;
            }
        }

        return longest;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            System.out.println(in + ": " + solution.longestPalindrome(in));
        }
        scanner.close();
    }
}
