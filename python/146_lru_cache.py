class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = ListNode(-1, -1)
        self.tail = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.map[key] if key in self.map else None

        if node:
            # Delete node to reattach to head
            if node.next:
                node.next.prev = node.prev

            node.prev.next = node.next

        self.replace_head(node)
        return node.val if node else -1

    def replace_head(self, node):
        if not node:
            return

        # Only move tail if there is more than one element
        if self.tail == node and node.prev != self.head:
            self.tail = node.prev

        # Original head
        head = self.head.next

        if head:
            head.prev = node
        else:
            # First element: assign tail
            self.tail = node

        node.prev = self.head
        node.next = head
        self.head.next = node
        self.map[node.key] = node

    def put(self, key: int, value: int) -> None:
        node = self.map[key] if key in self.map else None

        if node:
            node.val = value

            # Delete node to reattach to head
            if node.next:
                node.next.prev = node.prev

            node.prev.next = node.next
        else:
            # Delete least recently used
            if len(self.map) == self.capacity:
                tail = self.tail
                del self.map[tail.key]
                self.tail = tail.prev
                self.tail.next = None
                tail.prev = None

            node = ListNode(key, value)

        self.replace_head(node)


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(3)
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
obj.put(4,4)
print(obj.get(4))
print(obj.get(3))
print(obj.get(2))
print(obj.get(1))
obj.put(5,5)
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
print(obj.get(5))