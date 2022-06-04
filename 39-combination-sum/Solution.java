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

            while (c * x <= target) {
                for (int j = 0; j < x; j++) {
                    cur.addLast(c);
                }

                if (findSum(ans, candidates, target, i + 1, cur, sum + c * x)) {
                    ans.add(new ArrayList<>(cur));
                }

                for (int j = 0; j < x; j++) {
                    cur.removeLast();
                }

                x++;
            }
        }

        return false;
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new LinkedList<>();
        Arrays.sort(candidates);
        findSum(ans, candidates, target, 0, new LinkedList<>(), 0);
        return ans;
    }

    public static void main(String[] args) {
    Solution solution = new Solution();
       int[] candidates = {2,3,5};
       int target = 8;
       System.out.println(solution.combinationSum(candidates, target));
    }
}