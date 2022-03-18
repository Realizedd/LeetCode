import java.util.Scanner;

public class Solution {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public boolean isPalindrome(ListNode head) {
        if (head.next == null) {
            return true;
        } else if (head.next.next == null) {
            return head.val == head.next.val;
        }

        ListNode cur = head;
        int size = 0;

        // Calculate the size of the LL
        while (cur != null) {
            size++;
            cur = cur.next;
        }

        ListNode prev = null;
        cur = head;
        int index = 0;

        ListNode mid = null;

        while (cur != null) {
            if (index == size / 2) {
                if (size % 2 == 0) {
                    mid = cur;
                } else {
                    mid = cur.next;
                }

                break;
            }

            index++;
            
            ListNode temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }

        cur = prev;

        for (int i = 0; i < size / 2; i++) {
            if (mid.val != cur.val) {
                return false;
            }

            cur = cur.next;
            mid = mid.next;
        }

        return true;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String in = scanner.next();
            ListNode head = null;
            ListNode cur = null;
            
            for (String s : in.trim().replace("[", "").replace("]", "").split(",")) {
                System.out.println(s);
                int val = Integer.valueOf(s);
                if (head == null) {
                    head = new ListNode(val);
                    cur = head;
                } else {
                    cur.next = new ListNode(val);
                    cur = cur.next;
                }
            }

            cur = head;

            while (cur != null) {
                cur = cur.next;
            }
            
            System.out.println(in + ": " + solution.isPalindrome(head));
        }
        scanner.close();
    }   
}