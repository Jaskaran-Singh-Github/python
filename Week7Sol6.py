class MyQueue:
    def __init__(self):
        self.s1 = []  # Stack for pushing elements
        self.s2 = []  # Stack for popping elements

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:  # Transfer elements if s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

    def peek(self) -> int:
        if not self.s2:  # Ensure s2 has elements
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1] if self.s2 else None

    def empty(self) -> bool:
        return not self.s1 and not self.s2

# Example Usage
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # Output: 1
print(queue.pop())   # Output: 1
print(queue.empty()) # Output: False
