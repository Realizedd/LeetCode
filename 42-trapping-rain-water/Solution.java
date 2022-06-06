public class Solution {

    public int trap(int[] height) {
        if (height.length < 3) {
            return 0;
        }

        int maxHeightIndex = 0;
        int maxHeight = height[0];
        int total = 0;
        int curTotal = 0;

        for (int i = 1; i < height.length; i++) {
            int h = height[i];

            if (h > maxHeight) {
                maxHeight = h;
                maxHeightIndex = i;
                curTotal = 0;
            } else {
                int amount = maxHeight - h;
                total += amount;
                curTotal += amount;
            }
        }

        int lastHeight = height[height.length - 1];

        if (lastHeight < maxHeight) {
            total -= curTotal;

            int rMaxHeight = lastHeight;
            int rTotal = 0;

            for (int i = height.length - 2; i >= maxHeightIndex; i--) {
                int h = height[i];

                if (h > rMaxHeight) {
                    rMaxHeight = h;
                } else {
                    rTotal += rMaxHeight - h;
                }
            }

            total += rTotal;
        }

        return total;
    }

    public static void main(String[] args) {
        int[] height = {11,0,0,3,1,1,1,0,3,1,0,3,7,1,3,11,1,1,5,2,1,3,1,0,8};
        Solution solution = new Solution();
        System.out.println(solution.trap(height));
    }
}
