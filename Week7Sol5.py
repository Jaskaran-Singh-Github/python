from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft()  # Last element in q1 is the top of the stack
        self.q1, self.q2 = self.q2, self.q1  # Swap q1 and q2
        return top_element

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft()
        self.q2.append(top_element)  # Push it back since we are just peeking
        self.q1, self.q2 = self.q2, self.q1  # Swap q1 and q2
        return top_element

    def empty(self) -> bool:
        return not self.q1

# Example Usage
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())   # Output: 2
print(stack.pop())   # Output: 2
print(stack.empty()) # Output: False
