import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Solution {
    
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = null;
        ListNode cur = null;
        ListNode[] lists = {list1, list2};

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
