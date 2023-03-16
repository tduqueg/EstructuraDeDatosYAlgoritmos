class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
    

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    

    #Esta operación permite insetar items al final de la lista enlazasa
    #De manera que podamos manipular el nodo en la cola con una complejidad de O(1)
    def insert(self,data):
        
        new_node = Node(data)

        #Cuando la lista está vacía
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #Si hay al menos un item en la lista
        #Colocamos los items al final de la lista
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    #Podemos navegar por la lista doblemente enlazada en las dos direcciones
    def traverse_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        
        actual_node = self.tail

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous

if __name__ == "__main__":
    list = DoubleLinkedList() 
    list.insert(1)
    list.insert(2)
    list.insert(3)
    list.insert(4)
    list.insert(5)
    list.traverse_forward()
    list.traverse_backward()

