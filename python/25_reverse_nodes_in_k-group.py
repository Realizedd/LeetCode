# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head

        start = sentinel
        prev, cur = sentinel, head
        count = k

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            count -= 1

            if count == 0:
                count = k
                last = start.next
                start.next = cur
                start = last
                prev = start
                last.next = temp

            cur = temp

        if count < k:
            # temp = start.next
            # start.next = prev
            # temp.next = None
            # count = k - count
            prev, cur = None, prev

            while cur != start:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                # count -= 1

        return sentinel.next


sol = Solution()
ls = h = ListNode(1)
ls.next = ls = ListNode(2)
ls.next = ls = ListNode(3)
ls.next = ls = ListNode(4)
ls.next = ls = ListNode(5)
ls.next = ListNode(6)
c = sol.reverseKGroup(h, 4)

while c:
    print(c.val)
    c = c.next


