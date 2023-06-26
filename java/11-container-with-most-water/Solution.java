public class Solution {

    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1;
        int max = Math.min(height[r], height[l]) * (r - l);

        while (l < r) {
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }

            max = Math.max(max, Math.min(height[r], height[l]) * (r - l));
        }

        return max;
    }
}