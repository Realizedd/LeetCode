import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {

    private static final Map<Character, Integer> ROMAN_TO_INTEGER;

    static {
        ROMAN_TO_INTEGER = new HashMap<>();
        ROMAN_TO_INTEGER.put('I', 1);
        ROMAN_TO_INTEGER.put('V', 5);
        ROMAN_TO_INTEGER.put('X', 10);
        ROMAN_TO_INTEGER.put('L', 50);
        ROMAN_TO_INTEGER.put('C', 100);
        ROMAN_TO_INTEGER.put('D', 500);
        ROMAN_TO_INTEGER.put('M', 1000);
    }

    public int romanToInt(String s) {
        int sum = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int value = ROMAN_TO_INTEGER.get(s.charAt(i));

            if (i > 0) {
                int prev = ROMAN_TO_INTEGER.get(s.charAt(i - 1));

                if (prev < value) {
                    sum -= 2 * prev;
                }
            }

            sum += value;
        }

        return sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            System.out.println(in + ": " + solution.romanToInt(in));
        }
        scanner.close();
    }   
}