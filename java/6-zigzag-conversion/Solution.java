import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Solution {

    public String convert(String s, int numRows) {
        int length;

        if (numRows <= 1 || numRows > (length = s.length())) {
            return s;
        }

        String[] ans = new String[numRows];
        
        int row = 0;
        boolean inverse = false;

        for (int i = 0; i < length; i++) {
            if (ans[row] == null) {
                ans[row] = "";
            }

            ans[row] += s.charAt(i);

            if (inverse) {
                row--;

                if (row == 0) {
                    inverse = false;
                }
            } else {
                row++;

                if (row == numRows - 1) {
                    inverse = true;
                }
            }
        }

        return Arrays.stream(ans).collect(Collectors.joining());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            System.out.println(in + ": " + solution.convert(in, 2));
        }
        scanner.close();
    }
}
