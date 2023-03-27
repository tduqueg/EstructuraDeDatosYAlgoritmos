
class Vertex:

    #Esta clase representa los nodos o los grafos V
    def __init__(self, name):
        
        self.name = name
        # Es la representación del nodo en los conjuntos disjuntos
        self.node = None
    
class Edge:

    def __init__(self,weight, start_vertex, target_vertex):

        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
    
    #El algoritmo de Kruskal organiza los ejes o las conexiones por sus pesos
    #Por lo que Python debe saber como comparar pesos de conexiones
    def __lt__(self, other):

        return self.weight < other.weight
    

class Node:

    #Este es el nodo en la representación del árbol
    def __init__(self,rank, node_id, parent=None):
        #Rank es igual a la altura de un árbol
        self.rank = rank
        self.node_id = node_id
        self.parent = parent

class DisJointSet:

    def __init__(self, vertex_list):

        self.vertex_list = vertex_list
        #Estos son los nodos raíces (Representativos) de los conjuntos disjuntos
        self.root_nodes = []
        #Creamos tantos conjuntos disjuntos como vertices haya en el grafo
        self.make_sets()
    
    def make_sets(self):

        for v in self.vertex_list:
            
            node = Node(0,len(self.root_nodes))
            v.node = node
            self.root_nodes.append(node)

    #El objetivo de esta función es de encontrar el nodo representativo del conjunto disjunto dado
    def find(self,node):

        #Primero tenemos que encontrar el nodo raíz(representativo del conjunto disjunto dado)
        current_node = node

        while current_node.parent is not None:
            
            current_node = current_node.parent
        
        #Aplicamos compresión del camino
        root = current_node
        current_node = node

        #Tenemos que asegurarnos de que todos los nodos apunten al nodo raíz
        while current_node is not root:

            temp = current_node.parent
            current_node.parent = root
            current_node = temp
        
        return root.node_id
    
    #Esta es la manera de unir dos nodos
    def merge(self,node1, node2):

        #Primero debemos encontrar los nodos representativos o raíces
        index1 = self.find(node1)
        index2 = self.find(node2)

        #Si los ítems están en el mismo conjunto disjunto no se deben juntar
        if index1 == index2:
            return
        
        #Tenemos que hacer merge dependiendo de los ranks de cada nodo
        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]

        if root1.rank < root2.rank:
            
            root1.parent = root2
        
        elif root1.rank > root2.rank:
            root2.parent = root1
        
        else:
            root1.parent = root2
            root2.rank += 1

class KruskalAlgorithm:

    def __init__(self, vertex_list, edge_list):

        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def find_mst(self):

        disjoint_set = DisJointSet(self.vertex_list)
        mst = []


        #Algoritmo MST
        #Organizamos las conexiones dependiendo de su peso
        self.edge_list.sort()

        #Consideramos las conexiones de manera organizada
        for edge in self.edge_list:

            u = edge.start_vertex
            v = edge.target_vertex

            #Los nodos asociados con u y v nodos están en el mismo conjunto disjunto 
            #o no (Si comparten el mismo nodo raíz)
            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                
                mst.append(edge)

                #Tenemos ue combinar los conjuntos disjuntos
                disjoint_set.merge(u.node, v.node)
        
        for edge in mst:

            print(edge.start_vertex.name, ' - ', edge.target_vertex.name,' - ',edge.weight)

if __name__ == '__main__':

    #Vertices del grafo
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")

    # Conexiones
    edge1 = Edge(2, vertex1, vertex2)
    edge2 = Edge(6, vertex1, vertex3)
    edge3 = Edge(5, vertex1, vertex5)
    edge4 = Edge(10, vertex1, vertex6)
    edge5 = Edge(3, vertex2, vertex4)
    edge6 = Edge(3, vertex2, vertex5)
    edge7 = Edge(1, vertex3, vertex4)
    edge8 = Edge(2, vertex3, vertex6)
    edge9 = Edge(4, vertex4, vertex5)
    edge10 = Edge(5, vertex4, vertex7)
    edge11 = Edge(5, vertex6, vertex7)

    # Creamos las listas de los vertices y las conexiones
    vertices = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7]
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11]

    # Corremos el algoritmo para encontrar el mst(minimum spanning tree)
    algorithm = KruskalAlgorithm(vertices, edges)
    algorithm.find_mst()



        





