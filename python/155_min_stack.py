class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or self.min_stack[len(self.min_stack) - 1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None

        val = self.stack.pop()

        if self.min_stack[len(self.min_stack) - 1] == val:
            self.min_stack.pop()

        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(2)
obj.push(5)
obj.push(2)

print(obj.getMin(), obj.top())
obj.pop()
print(obj.getMin(), obj.top())
obj.pop()
print(obj.getMin(), obj.top())
obj.pop()
print(obj.getMin(), obj.top())
obj.pop()
print(obj.getMin(), obj.top())
