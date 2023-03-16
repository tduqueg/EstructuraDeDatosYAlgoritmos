class Queue:

    def __init__(self):
        self.entry_stack = []
        self.exit_stack = []
    
    def enqueue(self,data):
        self.entry_stack.append(data)

    def dequeue(self):

        if not self.exit_stack:
            while self.entry_stack:
                self.exit_stack.append(self.entry_stack.pop())
        if not self.exit_stack:
            return None
        return self.exit_stack.pop()
    
    def is_empty(self):
        return not self.entry_stack and not self.exit_stack
    
q = Queue()

q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.enqueue(9)
print("Dequeue: %d" % q.dequeue())
print("Dequeue: %d" % q.dequeue())
print("Dequeue: %d" % q.dequeue())
q.enqueue(8)
print("Dequeue: %d" % q.dequeue())
print("Dequeue: %d" % q.dequeue())
print("Dequeue: %d" % q.dequeue())
print(q.is_empty())
