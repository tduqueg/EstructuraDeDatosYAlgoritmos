class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None
    
    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        #Este es el primer nodo de la lista enlazada
        #Solo podemos acceder a este nodo!!
        self.head = None
        self.num_of_nodes = 0

    def find_middle_node(self):
        
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            slow_pointer = slow_pointer.next_node
            fast_pointer = fast_pointer.next_node.next_node

        print(slow_pointer)
        return slow_pointer

    def reverse(self):
        actual_pointer = self.head
        previous_pointer = None

        while actual_pointer is not None:
            next_pointer = actual_pointer.next_node
            actual_pointer.next_node = previous_pointer
            previous_pointer = actual_pointer
            actual_pointer = next_pointer
        self.head = previous_pointer



    #O(1)
    def insert_start(self,data):
        self.num_of_nodes += 1
        new_node = Node(data)
        #Esto es cuando no hay ningun nodo
        if self.head is None:
            self.head = new_node
        #Esto es cuando la lista enlazada no está vacía
        else:
            #Se tienen que actualizar las referencias o punteros
            new_node.next_node = self.head
            self.head = new_node
    #O(n)
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        #Hay que revisar si la Lista enlazada está vacía
        if self.head is None:
            self.head = new_node
        else:
            #Esto es cuando la lista enlazada no está vacía
            actual_node = self.head
            #Por esta razón la complejidad es de O(n) por que hay que pasar por cada uno de los nodos
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node


    def size_of_llinked_list(self):
        return self.num_of_nodes
    #O(n) tiempo de ejecución lineal
    def travese(self):
        
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node
    #O(n) tiempo de ejecución lineal
    def remove(self,data):

        if self.head is None:
            return
        #Necesitamos el nodo anterior para poder actualizar los punteros cuando se elimine un elemento
        actual_node = self.head
        previous_node = None
        #Buscamos el dato que queremos eliminar(data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
        #Si no encontramos el dato 
        if actual_node is None:
            return
        
        #Actualizamos los punteros o las referencias 
        #El nodo cabeza es el que queremos eliminar
        if previous_node is None:
            self.head = actual_node.next_node
            #Queremos eliminar un nodo interno
        else:
            #Borramos el nodo interno actualizando los punteros
            #No hay necesidad de borrar el nodo en si porque el GARBAGE COLLECTOR lo hará 
            previous_node.next_node = actual_node.next_node


        



if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start(9)
    linked_list.insert_start(2)
    linked_list.insert_end(230)
    linked_list.insert_end(50)
    linked_list.travese()
    print(50 * "-")
    linked_list.find_middle_node()
    print(50 * "-")
    linked_list.reverse()
    linked_list.travese()
