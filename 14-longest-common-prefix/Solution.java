public class Solution {

    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        
        String ans = strs[0];
        
        for (int i = 1; i < strs.length; i++) {
            String cur = strs[i];
            
            if (cur.length() < ans.length()) {  
                ans = ans.substring(0, cur.length());
            }

            for (int j = 0; j < ans.length(); j++) {
                if (j + 1 > ans.length()) {
                    break;
                }

                if (ans.charAt(j) != cur.charAt(j)) {
                    ans = ans.substring(0, j);
                }
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] arr = {"lkjhgfd", "lkjh", "lkjhguyt"};
        System.out.println(solution.longestCommonPrefix(arr));
    }
    
}