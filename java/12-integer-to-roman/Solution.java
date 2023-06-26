import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {

    private static final Map<Integer, String> INTEGER_TO_ROMAN;

    static {
        INTEGER_TO_ROMAN = new LinkedHashMap<>();
        INTEGER_TO_ROMAN.put(1000, "M");
        INTEGER_TO_ROMAN.put(900, "CM");
        INTEGER_TO_ROMAN.put(500, "D");
        INTEGER_TO_ROMAN.put(400, "CD");
        INTEGER_TO_ROMAN.put(100, "C");
        INTEGER_TO_ROMAN.put(90, "XC");
        INTEGER_TO_ROMAN.put(50, "L");
        INTEGER_TO_ROMAN.put(40, "XL");
        INTEGER_TO_ROMAN.put(10, "X");
        INTEGER_TO_ROMAN.put(9, "IX");
        INTEGER_TO_ROMAN.put(5, "V");
        INTEGER_TO_ROMAN.put(4, "IV");
        INTEGER_TO_ROMAN.put(1, "I");
    }
    
    public String intToRoman(int num) {
        final StringBuilder ans = new StringBuilder();

        for (Map.Entry<Integer, String> entry : INTEGER_TO_ROMAN.entrySet()) {
            int count = num / entry.getKey();

            if (count > 0) {
                for (int i = 1; i <= count; i++) {
                    ans.append(entry.getValue());
                }
            }

            num %= entry.getKey();
        }

        return ans.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            System.out.println(in + ": " + solution.intToRoman(Integer.parseInt(in)));
        }
        scanner.close();
    }
}