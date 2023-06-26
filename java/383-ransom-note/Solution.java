import java.util.Scanner;

public class Solution {

    public boolean canConstruct(String ransomNote, String magazine) {
        int[] charCount = new int[26];

        for (int i = 0; i < magazine.length(); i++) {
            charCount[magazine.charAt(i) - 'a']++;
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            int index = ransomNote.charAt(i) - 'a';

            if (charCount[index] == 0) {
                return false;
            }

            charCount[index]--;
        }
        
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String ransomNote = scanner.next();
            String magazine = scanner.next();
            System.out.println(solution.canConstruct(ransomNote, magazine));
        }
        scanner.close();
    }   
}