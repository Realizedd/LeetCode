public class Solution {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode cur = head;
        boolean add = false;

        while (l1 != null || l2 != null) {
            if (add) {
                cur.val += 1;
                add = false;
            }

            int sum = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0);

            cur.val += sum;

            if (cur.val >= 10) {
                cur.val -= 10;
                add = true;
            }

            if (l1 != null) {
                l1 = l1.next;
            }
        
            if (l2 != null) {
                l2 = l2.next;
            }

            if (l1 != null || l2 != null) {
                cur.next = new ListNode();
                cur = cur.next;
            } else if (add) {
                cur.next = new ListNode(1);
            }
        }

        return head;
    }
}