import java.util.regex.Pattern;

public class Solution {

    private static final Pattern FIRST_CHAR = Pattern.compile("[\\.\\+\\-0-9]");
    private static final Pattern CHAR = Pattern.compile("[\\+-\\.eE0-9]");

    public boolean isNumber(String s) {
        int len = s.length();

        if (len == 0) {
            return false;
        }

        boolean deci = false;
        boolean hasDigit = false;
        char ch = s.charAt(0);
        String c = Character.toString(ch);

        if (!FIRST_CHAR.matcher(c).matches()) {
            return false;
        }

        if (len == 1) {
            return !(s.equals("+") || s.equals("-") || s.equals("."));
        }

        if (c.equals(".")) {
            deci = true;
        }

        if (Character.isDigit(ch)) {
            hasDigit = true;
        }

        boolean e = false;
        int eIndex = -1;

        for (int i = 1; i < len; i++) {
            ch = s.charAt(i);

            if (Character.isDigit(ch)) {
                hasDigit = true;
            }
    
            c = Character.toString(ch);

            if (!CHAR.matcher(c).matches()) {
                return false;
            }

            if (c.equals(".")) {
                if (deci || e) {
                    return false;
                }

                deci = true;
            }

            if (c.equalsIgnoreCase("e")) {
                if (e || i == len - 1 || (i == 1 && !hasDigit)) {
                    return false;
                }

                e = true;
                eIndex = i;
            }

            if ((c.equals("+") || c.equals("-"))) {
                if (eIndex == -1 || i != eIndex + 1 || i == len - 1) {
                    return false;
                }
            }
        }

        return hasDigit;
    }

    public static void main(String[] args) {
        String[] valid = {"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"};
        String[] invalid = {"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "..", ".1e", "4e+", "+.", ".+"};
        Solution solution = new Solution();

        for (String s : valid) {
            System.out.println("[valid] " + s + ": " + solution.isNumber(s));
        }
        
        for (String s : invalid) {
            System.out.println("[invalid] " + s + ": " + solution.isNumber(s));
        }
    }
}
