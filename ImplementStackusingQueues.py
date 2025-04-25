from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft() if self.q1 else -1

    def top(self) -> int:
        return self.q1[0] if self.q1 else -1

    def empty(self) -> bool:
        return not self.q1

