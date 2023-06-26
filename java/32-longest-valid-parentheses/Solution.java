import java.util.Stack;

public class Solution {

    public int longestValidParentheses(String s) {
        if (s == null || s.length() < 2) {
            return 0;
        }

        int longest = 0;
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    if (s.charAt(stack.peek()) == '(') {
                        stack.pop();
                        longest = Math.max(i - (stack.isEmpty() ? -1 : stack.peek()), longest);
                    } else {
                        stack.push(i);
                    }
                }
            }
        }

        return longest;
    }
}