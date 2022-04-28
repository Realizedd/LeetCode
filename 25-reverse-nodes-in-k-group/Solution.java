public class Solution {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null) {
            return null;
        }

        if (head.next == null || k <= 1) {
            return head;
        }

        ListNode cur = head;
        int n = 0;

        while (cur != null) {
            n++;
            cur = cur.next;
        }

        cur = head;
        ListNode prev = null;
        ListNode beforeFirst = null;
        ListNode first = cur;

        for (int i = 1; i <= n / k; i++) {
            first = cur;

            for (int j = 0; j < k; j++) {
                ListNode temp = cur.next;
                cur.next = prev;
                prev = cur;
                cur = temp;
            }

            if (beforeFirst == null) {
                head = prev;
            } else {
                beforeFirst.next = prev;
            }
            
            first.next = cur;
            beforeFirst = first;
        }

        return head;
    }
}
