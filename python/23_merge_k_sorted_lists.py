# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            new_list = []
            n = len(lists)

            for i in range(0, n, 2):
                first = lists[i]
                second = lists[i + 1] if i + 1 < n else []
                new_list.append(self.mergeTwoLists(first, second))

            lists = new_list
            print(lists)

        return lists[0] if lists else None
