# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        tail = head
        cur = head

        while cur:
            tail = cur
            cur = cur.next

        sentinel, last = ListNode(next=head), ListNode()
        prev = sentinel
        cur = head
        end = last

        while cur and prev != tail:
            temp = cur.next

            if cur.val > x:
                prev.next = temp
                cur.next = None
                end.next = cur
                end = end.next
            else:
                prev = cur

            cur = temp

        prev.next = last.next
        return sentinel.next
