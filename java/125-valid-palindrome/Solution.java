import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    private char checkAlphanumeric(char c) {
        if ((48 <= c && c <= 57) || (97 <= c && c <= 122)) {
            return c;
        } else if ((65 <= c && c <= 90)) {
            return (char) (c + 32);
        } else {
            return 0;
        }
    }

    public boolean isPalindrome(String s) {
        char[] arr = s.toCharArray();
        int shift = 0;

        for (int i = 0; i < arr.length; i++) {
            if ((arr[i] = checkAlphanumeric(arr[i])) == 0) {
                shift++;
            } else {
                arr[i - shift] = arr[i];
            }
        }

        for (int i = 0; i < (arr.length - shift) / 2; i++) {
            if (arr[i] != arr[(arr.length - shift) - i - 1]) {
                return false;
            }
        }

        return true;
    }
}
