import java.util.Stack;

public class Solution {

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(' || c == '{' || c == '[') {
                stack.add(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }

                char m = stack.pop();

                if ((c == ')' && m != '(') || (c == '}' && m != '{') || (c == ']' && m != '[')) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
