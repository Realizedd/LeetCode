import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    
    // Lambda Sol.
    public int maximumWealthLambda(int[][] accounts) {
        return Arrays.stream(accounts).map(account -> Arrays.stream(account).sum()).max(Comparator.comparing(x -> x)).get();
    }

    public int maximumWealth(int[][] accounts) {
        int max = 0;

        for (int[] account : accounts) {
            int wealth = 0;

            for (int amount : account) {
                wealth += amount;
            }

            if (wealth > max) {
                max = wealth;
            }
        }

        return max;
    }

    public static void main(String[] args) {
        int[][] arr = {
            {1, 2, 3, 4, 5},
            {5, 2, 6, 7, 2}
        };
        Solution solution = new Solution();
        System.out.println(solution.maximumWealth(arr));
    }
}
