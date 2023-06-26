public class Solution {

    public String addBinary(String a, String b) {
        char[] arr = a.toCharArray();
        char[] brr = b.toCharArray();
        char[] min = arr.length > brr.length ? brr : arr;
        char[] max = arr.length > brr.length ? arr : brr;

        for (int i = max.length - 1, j = min.length - 1; i >= 0; i--, j--) {
            int sum;
            
            if ((sum = Character.digit(max[i], 10) + (j < 0 ? 1 : (Character.digit(min[j], 10) + 1))) > 1) {
                max[i] = sum > 2 ? '1' : '0';
            } else {
                max[i] = '1';
                return String.valueOf(max);
            }
        }

        char[] ans = new char[max.length + 1];
        ans[0] = '1';

        for (int i = 1; i < ans.length; i++) {
            ans[i] = '0';
        }

        return String.valueOf(ans);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String a =
                "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
                b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
        System.out.println(solution.addBinary(a, b));
    }
}
