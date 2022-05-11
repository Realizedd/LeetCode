import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
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
                    Set<Character> set = new HashSet<>();
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

        while (!possibleValues.isEmpty()) {
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

            Iterator<Map.Entry<String, Set<Character>>> iterator = possibleValues.entrySet().iterator();

            while (iterator.hasNext()) {
                Map.Entry<String, Set<Character>> entry = iterator.next();
    
                System.out.println(entry.getKey() + ": " + entry.getValue());

                if (entry.getValue().size() <= 1) {
                    iterator.remove();

                    if (!entry.getValue().isEmpty()) {
                        board[Character.getNumericValue(entry.getKey().charAt(0))][Character.getNumericValue(entry.getKey().charAt(1))] = entry.getValue().iterator().next();
                    }
                }
            }
        }
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