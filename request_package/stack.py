from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):

    def __init__(self):
        self.items = []

    def push(self, item: T):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]