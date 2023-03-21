import heapq

class Edge:

    def __init__(self,weight,start_node,target_node):
        
        self.weight = weight
        self.start_node = start_node
        self.target_node = target_node


class Node:

    def __init__(self,name):

        self.name = name
        self.visited = False
        #Este es el nodo del que vinimos en el camino más corto
        self.predecessor = None
        #De esta manera podemos almacenar los hijos de cada nodo
        self.adjacency_list = []
        #Esta es la distancia mínima entre el nodo en el que se empieza hasta este nodo
        self.min_distance = float('inf')
    
    #Esta función le permite a Python comparar objetos
    #Después de haber insertado los objetos en el heap
    #El heap podrá comparar los objetos que le demos
    def __lt__(self, other):
        return self.min_distance < other.min_distance

class DijkstraAlgorithm:

    def __init__(self):

        #Es un heap binario y no un heap Fibonacci
        self.heap = []
    
    def calculate(self,start_node):

        #Inicializamos los vertices
        start_node.min_distance = 0
        heapq.heappush(self.heap, start_node)

        while self.heap:

            #Hacemos pop al nodo más cercano(con la menor min_distance)
            actual_node = heapq.heappop(self.heap)

            if actual_node.visited:
                continue

            #Debemos considerar los vecinos
            for edge in actual_node.adjacency_list:

                u = edge.start_node
                v = edge.target_node
                new_distance = u.min_distance + edge.weight

                #Significa que hay una distancia más corta al nodo v
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    #Actualizamos el heap
                    #Esta implementación tiene una complejidad de O(n) para encontrar el nodo que queremos actualizar
                    #Además tenemos una complejidad de O(logn) para manejar el heap otra vez [O(n) + O(logn) = O(n)]
                    #Pero si se implementarea un heap de Fibonacci esta complejidad se reduciría a O(1)
                    heapq.heappush(self.heap,v)
            
            actual_node.visited = True

    @staticmethod
    def get_shortest_path(node):

        print("El camino más corto al nodo %s " % node.name, "tiene un peso de %s " % str(node.min_distance))

        
        actual_node = node

        while actual_node is not None:
            print("%s" % actual_node.name)
            actual_node = actual_node.predecessor



if __name__ == "__main__":


    #Creamos los nodos
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    #Creamos las conecciones
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    # Creamos los vecinos
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node2.adjacency_list.append(edge6)
    node8.adjacency_list.append(edge7)
    node8.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node5.adjacency_list.append(edge11)
    node6.adjacency_list.append(edge12)
    node6.adjacency_list.append(edge13)
    node3.adjacency_list.append(edge14)
    node3.adjacency_list.append(edge15)
    node4.adjacency_list.append(edge16)

    # Corremos la aplicación
    algorithm = DijkstraAlgorithm()
    algorithm.calculate(node1)
    algorithm.get_shortest_path(node7)


