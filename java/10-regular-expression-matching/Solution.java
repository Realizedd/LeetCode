import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class Solution {

    class Group {

        private char c;
        private boolean extending;

        Group(char c) {
            this.c = c;
        }

        void setExtending() {
            extending = true;
        }

        int validate(int start, String s) {
            if (extending) {
                while (start >= 0 && (c == '.' || s.charAt(start) == c)) {
                    start--;
                }

                return start;
            } else {
                return (c == '.' || s.charAt(start) == c) ? --start : -2;
            }
        }
    }

    public boolean isMatch(String s, String p) {
        LinkedList<Group> groups = new LinkedList<>();
        Group prev = null;

        for (int i = 0; i < p.length(); i++) {
            char cur = p.charAt(i);

            if (cur == '*') {
                if (prev != null) {
                    prev.setExtending();
                }
            } else {
                groups.add(prev = new Group(cur));
            }
        }

        int index = s.length() - 1;
        Iterator<Group> iterator = groups.descendingIterator();

        while (iterator.hasNext()) {
            Group group = iterator.next();

            // Not a match as the entire string has already been validated but there is still a group to process.
            if (index < 0 && !group.extending) {
                System.out.println(1);
                return false;
            }

            if ((index = group.validate(index, s)) == -2) {
                System.out.println(2);
                return false;
            }
        }

        // Return true if the groups have validated the entire string.
        return index < 0;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            String pattern = scanner.next();
            System.out.println("\"" + in + "\" matches pattern \"" + pattern + "\"? " + solution.isMatch(in, pattern));
        }
        scanner.close();
    }
}