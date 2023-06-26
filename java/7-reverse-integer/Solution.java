import java.util.Scanner;

public class Solution {

    public int reverse(int x) {
        if (x == 0) {
            return 0;
        }

        int digits = x == Integer.MIN_VALUE ? 10 : (int) (Math.floor(Math.log10(Math.abs(x))) + 1);
        int result = x % 10;
        int rem;
        x /= 10;

        for (int i = 0; i < digits - 1; i++) {
            rem = x % 10;

            try {
                result = Math.multiplyExact(result, 10);
                result = Math.addExact(result, rem);
            } catch (ArithmeticException ex) {
                return 0;
            }
            x /= 10;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            System.out.println(in + ": " + solution.reverse(Integer.parseInt(in)));
        }
        scanner.close();
    }
}
