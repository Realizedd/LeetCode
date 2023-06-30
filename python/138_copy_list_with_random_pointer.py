# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        node_map = {head: Node(head.val)}

        prev = head
        cur = head.next

        while cur:
            node_map[cur] = Node(cur.val)
            node_map[prev].next = node_map[cur]
            prev = cur
            cur = cur.next

        cur = head

        while cur:
            if cur.random:
                node_map[cur].random = node_map[cur.random]

            cur = cur.next

        return node_map[head]
