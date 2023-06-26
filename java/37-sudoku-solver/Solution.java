import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Solution {

    public void solveSudoku(char[][] board) {
        Map<String, Set<Character>> possibleValues = new LinkedHashMap<>();
        Map<Integer, List<Set<Character>>> rowMap = new HashMap<>();
        Map<Integer, List<Set<Character>>> colMap = new HashMap<>();
        Map<Integer, List<Set<Character>>> sqMap = new HashMap<>();

        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board.length; col++) {
                char val = board[row][col];

                if (val == '.') {
                    Set<Character> set = new LinkedHashSet<>();
                    set.add('1');
                    set.add('2');
                    set.add('3');
                    set.add('4');
                    set.add('5');
                    set.add('6');
                    set.add('7');
                    set.add('8');
                    set.add('9');
                    possibleValues.put(row + "" + col, set);

                    List<Set<Character>> rowList = rowMap.get(row);

                    if (rowList == null) {
                        rowMap.put(row, rowList = new LinkedList<>());
                    }

                    rowList.add(set);

                    List<Set<Character>> colList = colMap.get(col);

                    if (colList == null) {
                        colMap.put(col, colList = new LinkedList<>());
                    }

                    colList.add(set);

                    int sq = 3 * (row / 3) + col / 3;
                    // System.out.printf("row=%d,col=%d,sq=%d\n",row,col,sq);

                    List<Set<Character>> sqList = sqMap.get(sq);

                    if (sqList == null) {
                        sqMap.put(sq, sqList = new LinkedList<>());
                    }

                    sqList.add(set);
                }
            }
        }

        
        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board.length; col++) {
                char val = board[row][col];

                if (val == '.') {
                    continue;
                }
                
                List<Set<Character>> rList = rowMap.get(row);
                    
                if (rList != null) {
                    rList.forEach(set -> set.remove(val));
                }

                List<Set<Character>> cList = colMap.get(col);
                    
                if (cList != null) {
                    cList.forEach(set -> set.remove(val));
                }

                int sq = 3 * (row / 3) + col / 3;
                List<Set<Character>> sList = sqMap.get(sq);
                    
                if (sList != null) {
                    sList.forEach(set -> set.remove(val));
                }
            }
        }

        boolean changed = true;

        // Reduce possibilities as much as possible
        while (!possibleValues.isEmpty() && changed) {
            changed = false;
            Iterator<Map.Entry<String, Set<Character>>> iterator = possibleValues.entrySet().iterator();

            while (iterator.hasNext()) {
                Map.Entry<String, Set<Character>> entry = iterator.next();
    
                // System.out.println(entry.getKey() + ": " + entry.getValue());

                if (entry.getValue().size() <= 1) {
                    changed = true;
                    iterator.remove();

                    if (!entry.getValue().isEmpty()) {
                        int row = Character.getNumericValue(entry.getKey().charAt(0));
                        int col = Character.getNumericValue(entry.getKey().charAt(1));
                        char val = entry.getValue().iterator().next();
                        board[row][col] = val;

                        List<Set<Character>> rList = rowMap.get(row);
                            
                        if (rList != null) {
                            rList.forEach(set -> set.remove(val));
                        }

                        List<Set<Character>> cList = colMap.get(col);
                            
                        if (cList != null) {
                            cList.forEach(set -> set.remove(val));
                        }

                        int sq = 3 * (row / 3) + col / 3;
                        List<Set<Character>> sList = sqMap.get(sq);

                        if (sList != null) {
                            sList.forEach(set -> set.remove(val));
                        }
                    }
                }
            }
        }

        solve(board, 0, 0, possibleValues);
    }

    public boolean solve(final char[][] board, int row, int col, final Map<String, Set<Character>> possibleValues) {
        if (col == 9) {
            col = 0;
            row++;
        }

        if (row == 9) {
            return true;
        }

        if (possibleValues.get(row + "" + col) == null) {
            return solve(board, row, col + 1, possibleValues);
        }
        
        for (char val : possibleValues.get(row + "" + col)) {
            if (isValid(board, row, col, val)) {
                board[row][col] = val;
    
                if (solve(board, row, col + 1, possibleValues)) {
                    return true;
                }

                board[row][col] = '.';
            }
        }
        return false;
    }

    private boolean isValid(char[][] board, int row, int col, char c){
        int regionRow = 3 * (row / 3);  //region start row
        int regionCol = 3 * (col / 3);    //region start col
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == c) return false; //check row
            if (board[row][i] == c) return false; //check column
            if (board[regionRow + i / 3][regionCol + i % 3] == c) return false; //check 3*3 block
        }
        return true;
    }

    public static void main(String[] args) {
        char[][] board = {
                {'.','.','9','7','4','8','.','.','.'},
                {'7','.','.','.','.','.','.','.','.'},
                {'.','2','.','1','.','9','.','.','.'},
                {'.','.','7','.','.','.','2','4','.'},
                {'.','6','4','.','1','.','5','9','.'},
                {'.','9','8','.','.','.','3','.','.'},
                {'.','.','.','8','.','3','.','2','.'},
                {'.','.','.','.','.','.','.','.','6'},
                {'.','.','.','2','7','5','9','.','.'}
        };

        for (int i = 0; i < 9; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
        Solution solution = new Solution();
        solution.solveSudoku(board);
        
        for (int i = 0; i < 9; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }
}