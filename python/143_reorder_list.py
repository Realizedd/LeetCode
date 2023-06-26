# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check for no or single element LL
        if not head or not head.next:
            return head

        prev = head
        cur = head.next
        prev.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rev = self.reverseList(slow)
        cur = head

        while cur is not slow:
            temp = cur.next
            cur.next = rev
            rev = rev.next
            prev = cur.next
            cur.next.next = rev if temp == slow else temp
            cur = temp

        return head
