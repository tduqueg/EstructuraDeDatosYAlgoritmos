
class Node:

    def __init__(self, name):

        self.name = name
        self.adjacency_list = []
        self.visited = False
    

def depth_first_search(node):

    node.visite = True
    print(node.name)

    for n in node.adjacency_list:
        if not n.visited:
            depth_first_search(n)

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
 


