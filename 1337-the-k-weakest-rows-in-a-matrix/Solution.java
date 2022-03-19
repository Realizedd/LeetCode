import java.util.Arrays;

public class Solution {

    private boolean isWeaker(int firstIndex, int secondIndex, int[] first, int[] second) {
        for (int i = 0; i < first.length; i++) {
            if (first[i] < second[i]) {
                return true;
            }
        }

        return firstIndex < secondIndex;
    }

    private boolean contains(int index, int[] indexes) {
        for (int i : indexes) {
            if (i == index) {
                return true;
            }
        }

        return false;
    }

    public int[] kWeakestRows(int[][] mat, int k) {
        int[] indexes = new int[k];

        for (int i = 0; i < k; i++) {
            int weakest = 0;

            for (int j = 0; j < mat.length; j++) {
                if (!contains(j, indexes) && isWeaker(j, weakest, mat[j], mat[weakest])) {
                    weakest = j;
                }
            }

            indexes[i] = weakest;
        }
        
        return indexes;
    }

    public static void main(String[] args) {
        int[][] arr = {
            {1,1,0,0,0},
            {1,1,1,1,0},
            {1,0,0,0,0},
            {1,1,0,0,0},
            {1,1,1,1,1}
        };
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.kWeakestRows(arr, 3)));
    }
}