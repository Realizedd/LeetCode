public class Solution {
    
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    // Compare One-By-One Solution.
    // TODO: Look into Divide and Conquer & PriorityQueue Solutions
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode head = null;
        ListNode cur = null;

        while (true) {
            ListNode min = null;
            int minIndex = -1;

            for (int i = 0; i < lists.length; i++) {
                ListNode list = lists[i];

                if (list == null) {
                    continue;
                }

                if (min == null || min.val > list.val) {
                    min = list;
                    minIndex = i;
                }
            }

            if (min != null) {
                if (head != null) {
                    cur.next = min;
                    cur = cur.next;
                } else {
                    head = min;
                    cur = head;
                }

                lists[minIndex] = lists[minIndex].next;
            } else {
                break;
            }
        }

        return head;
    }
}
