from dataclasses import dataclass
from request_package import Stack, Queue
@dataclass
class Request:
    id: int
    message: str
r1 = Request(1, "Login problem")
r2 = Request(2, "Payment problem")
stack = Stack[Request]()
stack.push(r1)
stack.push(r2)
print("Stack Peek:", stack.peek().message)
print("Stack Pop:", stack.pop().message)
queue = Queue[Request]()
queue.enqueue(r1)
queue.enqueue(r2)
print("Queue Front:", queue.front().message)
print("Queue Dequeue:", queue.dequeue().message)