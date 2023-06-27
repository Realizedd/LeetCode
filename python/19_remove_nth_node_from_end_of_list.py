# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        count = 0
        prev = None
        target = head
        cur = head

        while cur:
            count += 1

            if count > n:
                prev = target
                target = target.next

            cur = cur.next

        if target == head:
            return target.next

        prev.next = target.next
        return head



