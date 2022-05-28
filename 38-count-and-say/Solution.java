import java.util.Scanner;

public class Solution {

    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }

        StringBuilder res = new StringBuilder();
        String s = countAndSay(n - 1);
        int rep = 0;

        for (int i = 0; i < s.length(); i++) {
            rep++;

            if (i == s.length() - 1 || s.charAt(i) != s.charAt(i + 1)) {
                res.append(rep).append(s.charAt(i));
                rep = 0;
            }
        }

        return res.toString();   
    }

    public String countAndSayIterative(int n) {
        String s = "1";

        for (int i = 1; i < n; i++) {
            StringBuilder res = new StringBuilder();
            int rep = 0;

            for (int j = 0; j < s.length(); j++) {
                rep++;

                if (j == s.length() - 1 || s.charAt(j) != s.charAt(j + 1)) {
                    res.append(rep).append(s.charAt(j));
                    rep = 0;
                }
            }

            s = res.toString();
        }

        return s;   
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution solution = new Solution();

        while (scanner.hasNextInt()) {
            System.out.println(solution.countAndSayIterative(scanner.nextInt()));
        }

        scanner.close();
    }
}