public class Solution {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode cur = head;
        int size = 0;

        while (cur != null) {
            size++;
            cur = cur.next;
        }

        cur = head;
        ListNode prev = null;
        int i = size;

        while (cur != null) {
            if (i == n) {
                if (prev == null) {
                    head = cur.next;
                } else {
                    prev.next = cur.next;
                }
                return head;
            }

            prev = cur;
            cur = cur.next;
            i--;
        }

        return head;
    }
}