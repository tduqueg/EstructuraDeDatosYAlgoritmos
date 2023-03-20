
class Node:

    def __init__(self,name):
        
        self.name = name
        self.adjacency_list = []
        self.visited = False

def breadth_first_search(start_node):

    #FIFO 
    queue = [start_node]
    start_node.visited = True
    #Tenemos que seguir iterando sobre todos los nodos vecionas hasta que la cola este vacía
    while queue:

        #Eliminamos y devolvemos el primer ítem insertado en la lista
        actual_node = queue.pop(0)
        print(actual_node.name)

        #Debemos considerar los vecinos del nodo actual uno por uno
        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                queue.append(n)
                
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
    breadth_first_search(nodo1)

