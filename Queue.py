#FIFO First In First Out

class Queue:
    
    def __init__(self):
        self.queue = []

    #Devuelve True si la cola está vacía
    #Su complejidad es de O(1)
    def is_empty(self):
        return self.queue == []
    
    #Añade un dato a la cola
    #Su complejidad es de O(1)
    def enqueue(self,data):
        self.queue.append(data)

    #Devuelve el primer ítem y lo elimina
    #Su complejidad es de O(n)
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1
    #Devuelve el primer ítem
    #Su complejidad es de O(1)
    def peek(self):
        return self.queue[0]
    
    #Devuelve el tamaño de la cola
    #Su complejidad es de O(1)
    def size_queue(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Tamaño: %d" % q.size_queue())
print("Dequeue: %d" % q.dequeue())
print("Dequeue: %d" % q.dequeue())
print("Tamaño: %d" % q.size_queue())
    
    