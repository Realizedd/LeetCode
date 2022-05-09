public class Solution {

    public boolean isValidSudoku(char[][] board) {
        for (int sq = 0; sq < board.length; sq++) {        
            boolean[] rSet = new boolean[9];
            boolean[] cSet = new boolean[9];
            boolean[] sSet = new boolean[9];

            for (int cell = 0; cell < board.length; cell++) {
                char rVal = board[sq][cell];

                if (rVal != '.') {
                    int n = rVal - '0' - 1;
                    
                    if (!rSet[n]) {
                        rSet[n] = true;
                    } else {
                        return false;
                    }
                }
                
                char cVal = board[cell][sq];

                if (cVal != '.') {
                    int n = cVal - '0' - 1;
                    
                    if (!cSet[n]) {
                        cSet[n] = true;
                    } else {
                        return false;
                    }
                }

                char sVal = board[3 * (sq / 3) + cell / 3][3 * (sq % 3) + cell % 3];

                if (sVal != '.') {
                    int n = sVal - '0' - 1;

                    if (!sSet[n]) {
                        sSet[n] = true;
                    } else {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {
        char[][] board = {
                        {'5','3','.','.','7','.','.','.','.'},
                        {'6','.','.','1','9','5','.','.','.'},
                        {'.','9','8','.','.','.','.','6','.'},
                        {'8','.','.','.','6','.','.','.','3'},
                        {'4','.','.','8','.','3','.','.','1'},
                        {'7','.','.','.','2','.','.','.','6'},
                        {'.','6','.','.','.','.','2','8','.'},
                        {'.','.','.','4','1','9','.','.','5'},
                        {'.','.','.','.','8','.','.','7','9'}
        };
        Solution solution = new Solution();
        System.out.println(solution.isValidSudoku(board));
    }
}
