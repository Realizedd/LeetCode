import java.util.Scanner;

public class Solution {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode middleNode(ListNode head) {
        ListNode cur = head;
        ListNode mid = head;

        while (cur != null && cur.next != null) {
            cur = cur.next.next;
            mid = mid.next;
        }

        return mid;
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
            
            System.out.println("Middle of " + in + ": " + solution.middleNode(head).val);
        }
        scanner.close();
    }   
}