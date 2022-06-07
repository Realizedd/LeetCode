import java.util.Arrays;

public class Solution {

    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }

        int a = num1.length();
        int b = num2.length();

        String longer, shorter;
        int longerLength, shorterLength;

        if (a > b) {
            longer = num1;
            shorter = num2;
            longerLength = a;
            shorterLength = b;
        } else {
            longer = num2;
            shorter = num1;
            longerLength = b;
            shorterLength = a;
        }

        int[] ans = new int[a + b];

        for (int i = shorterLength - 1; i >= 0; i--) {
            for (int j = longerLength - 1; j >= 0; j--) {
                int pos = ans.length - 1 - ((shorterLength - i - 1) + (longerLength - j - 1));
                int added = Character.getNumericValue(shorter.charAt(i)) * Character.getNumericValue(longer.charAt(j));
                int val = ans[pos];
                val += added;
                int carry = val / 10;
                val -= 10 * carry;
                ans[pos] = val;

                while (carry > 0) {
                    --pos;
                    val = ans[pos] + carry;
                    carry = val > 10 ? 1 : 0;
                    val -= carry * 10;
                    ans[pos] = val;
                }
            }
        }

        System.out.println(Arrays.toString(ans));
        StringBuilder builder = new StringBuilder();
        boolean leading = true;

        for (int i = 0; i < ans.length; i++) {
            if (ans[i] > 0) {
                leading = false;
            } if (ans[i] == 0 && leading) {
                continue;
            }

            builder.append(ans[i]);
        }

        return builder.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.multiply("123", "456"));
    }
}