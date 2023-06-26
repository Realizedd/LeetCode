import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    private boolean findSum(List<List<Integer>> ans, int[] candidates, int target, int index, List<Integer> cur, int sum) {
        if (sum == target) {
            return true;
        } else if (sum > target) {
            return false;
        }

        for (int i = index; i < candidates.length; i++) {
            if (i > index && candidates[i] == candidates[i - 1]) {
                continue;
            }

            int c = candidates[i];

            if (sum + c > target) {
                break;
            }
            
            cur.add(c);

            if (findSum(ans, candidates, target, i + 1, cur, sum + c)) {
                List<Integer> sol = new ArrayList<>(cur.size());
                
                for (int n : cur) {
                    sol.add(n);
                }
                
                ans.add(sol);
            }

            cur.remove(cur.size() - 1);
        }

        return false;
    }
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(candidates);
        findSum(ans, candidates, target, 0, new ArrayList<>(), 0);
        return ans;
    }

    public static void main(String[] args) {
    Solution solution = new Solution();
       int[] candidates = {2,5,2,1,2};
       int target = 5;
       System.out.println(solution.combinationSum2(candidates, target));
    }
}