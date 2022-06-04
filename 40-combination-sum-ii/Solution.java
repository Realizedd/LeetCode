import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Solution {

    // TODO: VERY INEFFICIENT BRUTE FORCE SOLUTION - Work on optimizing
    private boolean findSum(List<List<Integer>> ans, int[] candidates, int target, int index, LinkedList<Integer> cur, int sum) {
        if (sum == target) {
            return true;
        } else if (sum > target) {
            return false;
        }

        for (int i = index; i < candidates.length; i++) {
            int c = candidates[i];
            int x = 1;

            while (i < candidates.length - 1 && candidates[i] == candidates[i + 1]) {
                x++;
                i++;
            }

            for (int k = 1; k <= x; k++) {
                for (int j = 0; j < k; j++) {
                    cur.addLast(c);
                }

                if (findSum(ans, candidates, target, i + 1, cur, sum + c * k)) {
                    ans.add(new ArrayList<>(cur));
                }

                for (int j = 0; j < k; j++) {
                    cur.removeLast();
                }
            }
        }

        return false;
    }
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new LinkedList<>();
        Arrays.sort(candidates);
        findSum(ans, candidates, target, 0, new LinkedList<>(), 0);
        return ans;
    }

    public static void main(String[] args) {
    Solution solution = new Solution();
       int[] candidates = {10,1,2,7,6,1,5};
       int target = 8;
       System.out.println(solution.combinationSum2(candidates, target));
    }
}