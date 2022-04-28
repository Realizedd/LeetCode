public class Solution {
    
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode swapPairs(ListNode head) {
        if (head == null) {
            return null;
        }

        if (head.next == null) {
            return head;
        }

        ListNode first = head, second = head.next;
        ListNode prev = null;

        while (first != null && second != null) {
            if (prev == null) {
                head = second;
            } else {
                prev.next = second;
            }           

            first.next = second.next;
            second.next = first;

            prev = first;
            first = first.next;
            second = first != null ? first.next : null;
        }

        return head;
    }
}