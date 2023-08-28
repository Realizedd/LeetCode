from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.cur_top = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.cur_top = x

    def pop(self) -> int:
        self.cur_top = None

        for _ in range(len(self.q1) - 1):
            self.cur_top = self.q1.popleft()
            self.q1.append(self.cur_top)

        return self.q1.popleft()

    def top(self) -> int:
        return self.cur_top

    def empty(self) -> bool:
        return not len(self.q1)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()