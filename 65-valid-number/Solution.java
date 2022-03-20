import java.util.regex.Pattern;

public class Solution {

    private static final Pattern FIRST_CHAR = Pattern.compile("\\+\\-[0-9]");
    private static final Pattern CHAR = Pattern.compile("\\+\\-\\.e[0-9]");

    public boolean isNumber(String s) {
        int len = s.length();

        if (len == 0) {
            return false;
        }

        if (!FIRST_CHAR.matcher(Character.toString(s.charAt(0))).matches()) {
            return false;
        }

        if (len == 1) {
            return !(s.equals("+") || s.equals("-"));
        }

        boolean e = false;
        int eIndex = -1;
        boolean deci = false;
        int deciIndex = -1;

        for (int i = 1; i < len; i++) {
            String c = Character.toString(s.charAt(i));

            if (!CHAR.matcher(c).matches()) {
                return false;
            }

            if (c.equals(".")) {
                if (deci) {
                    return false;
                }

                deci = true;
                deciIndex = i;
            }

            if (c.equals("e")) {
                if (e) {
                    return false;
                }

                e = true;
                eIndex = i;
            }

            if ((s.equals("+") || s.equals("-"))) {
                if (eIndex == -1) {
                    return false;
                }

                if (i != eIndex + 1) {
                    return false;
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String[] valid = {"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"};
        Solution solution = new Solution();

        for (String s : valid) {
            System.out.println(s + ": " + solution.isNumber(s));
        }
    }
}
