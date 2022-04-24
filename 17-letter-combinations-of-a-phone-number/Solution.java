import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Solution {

    private static final char[][] MAPPINGS = {
        {'a', 'b', 'c'}, // 2
        {'d', 'e', 'f'}, // 3
        {'g', 'h', 'i'}, // 4
        {'j', 'k', 'l'}, // 5
        {'m', 'n', 'o'}, // 6
        {'p', 'q', 'r', 's'}, // 7
        {'t', 'u', 'v'}, // 8
        {'w', 'x', 'y', 'z'} // 9
    };

    public List<String> letterCombinations(String digits) {
        List<String> combinations = new LinkedList<>();

        if (digits.length() == 0) {
            return combinations;
        }

        for (int i = 0; i < digits.length(); i++) {
            char[] chars = MAPPINGS[(int) (digits.charAt(i) - '0') - 2];

            List<String> updated = new LinkedList<>();

            for (int j = 0; j < chars.length; j++) {
                if (i == 0) {
                    updated.add(Character.toString(chars[j]));
                    continue;
                }

                for (int k = 0; k < combinations.size(); k++) {
                    updated.add(new StringBuilder(combinations.get(k)).append(chars[j]).toString());
                }
            }

            combinations = updated;
        }

        return combinations;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            System.out.println(in + ": " + solution.letterCombinations(in));
        }
        scanner.close();
    }
}