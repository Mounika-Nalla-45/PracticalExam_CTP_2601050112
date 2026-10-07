from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):

    def __init__(self):
        self.items = []

    def enqueue(self, item: T):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def front(self):
        if not self.items:
            return None
        return self.items[0]