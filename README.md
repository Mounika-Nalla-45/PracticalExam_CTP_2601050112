# Stack and Queue Using Python Package

## 9. Question

A customer-support application needs reusable data structures to manage customer requests. Customer requests should be handled using a Queue, while recently processed requests can be maintained using a Stack for undo/review operations.

**Task:** Develop a reusable Python package that implements Stack and Queue using type hints and dataclasses.

The package should:

* Define a generic Stack class using type hints.
* Define a generic Queue class using type hints.
* Use dataclass where appropriate for storing request information.
* Implement `push()`, `pop()`, and `peek()` for Stack.
* Implement `enqueue()`, `dequeue()`, and `front()` for Queue.
* Handle empty Stack/Queue conditions appropriately.
* Organize the implementation as a reusable Python package.
* Create a separate test/demo program to import and use the package.

---

## 2. Algorithm

### Stack

1. Create an empty list for storing elements.
2. Use `push()` to add an element.
3. Use `pop()` to remove the last element.
4. Use `peek()` to view the last element.
5. Return `None` if the Stack is empty.

### Queue

1. Create an empty list for storing elements.
2. Use `enqueue()` to add an element at the end.
3. Use `dequeue()` to remove the first element.
4. Use `front()` to view the first element.
5. Return `None` if the Queue is empty.

---

## 3. Program

### stack.py

```python
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
```

### queue.py

```python
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
```

### **init**.py

```python
from .stack import Stack
from .queue import Queue
```

### demo.py

```python
from dataclasses import dataclass
from request_package import Stack, Queue


@dataclass
class Request:
    id: int
    message: str


r1 = Request(1, "Login problem")
r2 = Request(2, "Payment problem")

# Stack
stack = Stack[Request]()
stack.push(r1)
stack.push(r2)

print("Stack Peek:", stack.peek().message)
print("Stack Pop:", stack.pop().message)

# Queue
queue = Queue[Request]()
queue.enqueue(r1)
queue.enqueue(r2)

print("Queue Front:", queue.front().message)
print("Queue Dequeue:", queue.dequeue().message)
```

---

## 4. Output

```text
Stack Peek: Payment problem
Stack Pop: Payment problem
Queue Front: Login problem
Queue Dequeue: Login problem
```


# 5. Viva Questions and Answers

### 1. What is a Stack?

A Stack is a data structure that follows **LIFO (Last In, First Out)**.

### 2. What is a Queue?

A Queue is a data structure that follows **FIFO (First In, First Out)**.

### 3. What are the operations used in Stack ?

Stack uses push(), pop(), and peek().

### 4. What are the operations used in Queue ?

Queue uses enqueue(), dequeue(), and front().

### 5. What is the time complexity of Stack and Queue operations?

Stack operations are O(1). Queue enqueue() and front() are O(1), while dequeue() is O(n) in this program.
