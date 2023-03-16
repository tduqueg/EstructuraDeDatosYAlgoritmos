#LIFO Last In First Out

class Stack:
    
    def __init__(self):
        self.stack = []
        self.max_stack = []

    #Inserta items en el stack 
    #Su complejidad es de O(1)
    def push(self,data):
        self.stack.append(data)
        if not self.max_stack or data >= self.max_stack[-1]:
            self.max_stack.append(data)
    
    #Elimina y devuelve el último item de la pila
    #Su complejidad es de O(1)
    def pop(self):

        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()

        if self.stack_size()<1:
            return -1
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    #Devuelve el último ítem sin eliminarlo
    #Su complejidad es de O(1)
    def peek(self):
        return self.stack[-1]
    
    #Chequea si la pila está vacía
    #Su complejidad es de O(1)
    def is_empty(self):
        return self.stack == []
    
    def stack_size(self):
        return len(self.stack)
    
    def max(self):
        return self.max_stack[-1]

stack = Stack()
stack.push(601)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(600)
stack.push(4)
stack.push(5)
print("Tamaño: %d" % stack.stack_size())
print("Elemento Eliminado %d" % stack.pop())
print("Elemento Eliminado %d" % stack.pop())
print("Elemento Eliminado %d" % stack.pop())
print("Elemento Eliminado %d" % stack.pop())
print("Elemento Solicitado %d" % stack.peek())
print("Elemento más grande %d" % stack.max())




    