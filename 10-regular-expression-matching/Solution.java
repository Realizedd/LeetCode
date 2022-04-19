import java.util.Scanner;

public class Solution {

    public boolean isMatch(String s, String p) {
        int j = 0, c = 0;

        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            char curPattern = p.charAt(j);

            if (p.charAt(j) == '*') {
                if (cur != p.charAt(j - 1) && p.charAt(j - 1) != '.') {
                    if (j + 1 < p.length()) {
                        j++;
                        i--;    
                    } else {
                        System.out.println("No more characters remaining in pattern");
                        return false;
                    }
                }

                c++;
                continue;
            }
            
            System.out.println(cur + " - " + curPattern);

            if (cur != curPattern && curPattern != '.') {
                System.out.println("Character does not match 1-to-1");
                return false;
            }

            if (j + 1 < p.length()) {
                j++;
            } else if (i + 1 != s.length()) {
                System.out.println("Character does not match 1-to-1 and this is not the last iteration");
                return false;
            }

            c++;
        }

        if (c < p.length()) {
            System.out.println("Does not match the whole pattern");
            return false;
        }

        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            String pattern = scanner.next();
            System.out.println("\"" + in + "\" matches pattern \"" + pattern + "\"? " + solution.isMatch(in, pattern));
        }
        scanner.close();
    }
}