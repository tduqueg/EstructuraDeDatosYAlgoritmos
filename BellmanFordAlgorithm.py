
class Edge:

    def __init__(self, weight, start_vertex, target_vertex):

        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    
    def __init__(self, name):

        self.name = name
        self.adjacency_list = []
        self.predecessor = None
        self.min_distance = float('inf')
    

class BellmanFordAlgorithm:

    def __init__(self, vertex_list, edge_list, start_vertex):

        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False

    def find_shortest_path(self):

        self.start_vertex.min_distance = 0

        #Consideramos V-1 iteraciones
        #La complejidad de este es de O(V*E)
        for _ in range(len(self.vertex_list)-1):

            #En cada iteración consideramos todas las conexiones
            for edge in self.edge_list:

                #Calculamos si hay un camino más corto
                u = edge.start_vertex
                v = edge.target_vertex
            
                dist = u.min_distance + edge.weight

                if dist < v.min_distance:
                    v.predecessor = u
                    v.min_distance = dist
        
        #Después de haber hecho V-1 iteraciones tenemos que revisar si hay ciclos negativos
        for edge in self.edge_list:
            if self.check_cycle(edge):
                print("Ciclo negtivo encontrado...")
                return
    
    def check_cycle(self, edge):
        
        #Si el total de la distancia mínima de un nodo dado decrementa despues de V-1 iteraciones
        #Entonces hay un ciclo negativo
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:
        
            self.has_cycle = True
            return True
        else:
            return False
    
    def get_shortest_path(self,vertex):

        if not self.has_cycle:
            print('EL camino más corto existe con el valor: ', vertex.min_distance)
            node = vertex

            while node is not None:
                print(node.name)
                node = node.predecessor

        else:
            print('Hay un ciclo negativo en el grafo...')


if __name__ == '__main__':

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")


    edge1 = Edge(5, node1, node2)
    edge2 = Edge(9, node1, node5)
    edge3 = Edge(4, node2, node5)
    edge4 = Edge(12, node2, node3)
    edge5 = Edge(7, node2, node4)
    edge6 = Edge(3, node3, node4)
    edge7 = Edge(1, node3, node6)
    edge8 = Edge(9, node4, node7)
    edge9 = Edge(6, node5, node3)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(2, node6, node7)
    edge12 = Edge(6, node7, node3)

    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node2.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node3.adjacency_list.append(edge6)
    node3.adjacency_list.append(edge7)
    node4.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node6.adjacency_list.append(edge11)
    node7.adjacency_list.append(edge12)

    vertices = (node1, node2, node3, node4, node5, node6, node7)
    edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12)

    algorithm = BellmanFordAlgorithm(vertices, edges, node1)
    algorithm.find_shortest_path()
    algorithm.get_shortest_path(node7)


        
