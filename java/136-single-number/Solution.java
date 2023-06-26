public class Solution {

    public int singleNumber(int[] nums) {
        int[] arr = new int[60001];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.MIN_VALUE;
        }

        for (int i = 0; i < nums.length; i++) {
            int index = nums[i] + 30000;
            arr[index] = arr[index] == Integer.MIN_VALUE ? nums[i] : Integer.MIN_VALUE;

        }

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != Integer.MIN_VALUE) {
                return arr[i];
            }
        }

        return Integer.MIN_VALUE;
    }

    public int singleNumberXOR(int[] nums) {
        int a = nums[0];

        for (int i = 1; i < nums.length; i++) {
            a ^= nums[i];
        }

        return a;
    }

    public static void main(String[] args) {
        int[] arr = { 3, 5, 6, 2, 2, 5, 1, 3, 6 };
        Solution solution = new Solution();
        System.out.println(solution.singleNumber(arr));
    }
}
