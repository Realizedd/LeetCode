# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head or not head.next:
            return head

        sz = 0
        cur = head
        tail = None

        while cur:
            sz += 1
            tail = cur
            cur = cur.next

        k %= sz

        if not k:
            return head

        tail.next = head

        prev = None
        cur = head

        for _ in range(sz - k):
            prev = cur
            cur = cur.next

        prev.next = None
        return cur
