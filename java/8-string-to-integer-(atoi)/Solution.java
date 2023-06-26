import java.util.Scanner;

public class Solution {

    public int myAtoi(String s) {
        boolean neg = false, reachedDigit = false, reachedSign = false;
        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                if (!reachedDigit) {
                    reachedDigit = true;
                }

                try {
                    result = Math.multiplyExact(result, 10);
                    result = Math.addExact(result, c - '0');
                } catch (ArithmeticException ex) {
                    return neg ? Integer.MIN_VALUE : Integer.MAX_VALUE;
                }
            } else if (reachedDigit) {
                break;
            } else if (c == '+' || c == '-') {
                if (reachedSign) {
                    break;
                } else {
                    reachedSign = true;

                    if (c == '-') {
                        neg = true;
                    }
                }
            } else if (c == ' ') {
                if (reachedSign) {
                    break;
                }
            } else {
                break;
            }
        }

        return neg ? -result : result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.nextLine();
            System.out.println(in + ": " + solution.myAtoi(in));
        }
        scanner.close();
    }
}
