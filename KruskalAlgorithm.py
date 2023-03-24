
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

        





