public class Solution {

    // O(N) Solution
    public double _findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] merged = new int[m + n];
        
        for (int i = 0, j = 0, k = 0; i < m + n; i++) {
            if (j < m && k < n) {
                merged[i] = nums1[j] > nums2[k] ? nums2[k++] : nums1[j++];
            } else if (j < m) {
                merged[i] = nums1[j++];
            } else if (k < n) {
                merged[i] = nums2[k++];
            }
        }

        int midpoint = (m + n) / 2;

        if ((m + n) % 2 == 0) {
            return (merged[midpoint] + merged[midpoint - 1]) / 2.0;
        } else {
            return merged[midpoint];
        }
    }
    
    // GOAL: O(log n) Solution
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        return findMedianSortedArrays(nums1, 0, nums1.length - 1, nums2, 0, nums2.length - 1);
    }
    
    public double findMedianSortedArrays(int[] nums1, int p, int q, int[] nums2, int r, int s) {
        int m = p - q + 1;
        int n = r - s + 1;

        if (m <= 2 || n <= 2) {
            return (Math.max(nums1[p], nums2[r]) + Math.min(nums1[p + 1], nums2[r + 1])) / 2.0;
        }

        double m1, m2;

        if (m % 2 == 0) {
            m1 = (nums1[p + m / 2] + nums1[p + ((m / 2) - 1)]) / 2.0;
        } else {
            m1 = nums1[p + m / 2];
        }

        if (n % 2 == 0) {
            m2 = (nums2[r + n / 2] + nums2[r + ((n / 2) - 1)]) / 2.0;
        } else {
            m2 = nums2[r + n / 2];
        }

        if (m1 == m2) {
            return m1;
        } else if (m1 < m2) {
            return findMedianSortedArrays(nums1, p + m / 2, q, nums2, r, s - m / 2);
        } else {
            return findMedianSortedArrays(nums1, p, p + m / 2, nums2, r + m / 2, s);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {1, 5, 9, 16, 25, 200}, nums2 = {2, 3, 7, 13, 14, 18, 30, 202};
        System.out.println(solution.findMedianSortedArrays(nums1, nums2));
    }
}