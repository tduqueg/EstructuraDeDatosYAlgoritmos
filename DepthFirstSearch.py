
class Node:

    def __init__(self, name):

        self.name = name
        self.adjacency_list = []
        self.visited = False
    

def depth_first_search(start_node):

    #Necesitamos una estructura LIFO para implementarlo
    stack = [start_node]
    start_node.visited = True


    #Iterarem´ós sobre el stack hasta que este vacío
    while stack:

        #La función pop tiene una complejidad de tiempo de ejecución de O(1)
        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            #Queremos evitar que se visite una y otra vez el mismo nodo
            if not n.visited:
                stack.append(n)
                n.visited = True


if __name__ == '__main__':

       
    #Creamos los nodos(vertices)
    nodo1 = Node("A")
    nodo2 = Node("B")
    nodo3 = Node("C")
    nodo4 = Node("D")
    nodo5 = Node("E")

    #Asignamos los vecinos de cada nodo
    nodo1.adjacency_list.append(nodo2)
    nodo1.adjacency_list.append(nodo3)
    nodo2.adjacency_list.append(nodo4)
    nodo4.adjacency_list.append(nodo5)

    #Ejecutamos el algoritmo Breadth-First search
    depth_first_search(nodo1)
 


