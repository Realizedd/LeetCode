import java.util.Scanner;

public class Solution {

    private int atDigit(int x, int digit) {
        if (digit <= 0) {
            return 0;
        }

        x /= (int) Math.pow(10, digit - 1);
        return x % 10;
    }

    public boolean isPalindrome(final int x) {
        if (x < 0) {
            return false;
        }

        int digits = x == Integer.MIN_VALUE ? 10 : (int) (Math.floor(Math.log10(Math.abs(x))) + 1);
        int cp = x;

        for (int i = 0; i < digits / 2; i++) {
            if ((cp % 10) != atDigit(x, digits - i)) {
                return false;
            }

            cp /= 10;
        }

        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            System.out.println(in + ": " + solution.isPalindrome(Integer.parseInt(in)));
        }
        scanner.close();
    }
}