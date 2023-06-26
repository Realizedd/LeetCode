import java.util.LinkedList;
import java.util.List;

public class Solution {

    private void generate(List<String> result, int opening, int closing, String s) {
        if (opening == 0 && closing == 0) {
            result.add(s);
            return;
        }

        if (opening > 0) {
            generate(result, opening - 1, closing, s + "(");
        }

        if (opening < closing && closing > 0) {
            generate(result, opening, closing - 1, s + ")");
        }
    }

    public List<String> generateParenthesis(int n) {
        List<String> ans = new LinkedList<>();
        generate(ans, n, n, "");
        return ans;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.generateParenthesis(3));
    }
}