import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {

    // Sorting: O(nlog(n)) RC, O(1) SC
    public boolean containsDuplicateSorting(int[] nums) {
        Arrays.sort(nums);

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }

        return false;
    }

    // Hash Table: O(n) RC, O(n) SC
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (!set.add(nums[i])) {
                return true;
            }
        }

        return false;
    }
}
