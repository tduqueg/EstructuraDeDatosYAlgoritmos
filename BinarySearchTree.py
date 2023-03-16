
class Node:

    def __init__(self, data, parent = None):
        
        self.data = data
        self.left_node = None
        self.right_node = None
        # Esto es crucial para implementar la operación REMOVE 
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
     # Este es el único nodo al que tenemos acceso 
        self.root = None

    def insert(self, data):
    #Este es el primer nodo en el Árbol binario
        if self.root is None:
            self.root = Node(data)
    #Cuando el árbol no este vacío
        else:
            self.insert_node(data,self.root)

    def insert_node(self,data,node):
        #Debemos ir al subarbol izquierdo
        if data < node.data:
            if node.left_node:
                #El nodo izquierdo no existe, por lo que seguimos 
                self.insert_node(data, node.left_node)
            else:
                #Como no hay un hijo en la izquierda, creamos uno
                node.left_node = Node(data,node)
        #Debemos ir por el subarbol derecho
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else: 
                node.right_node = Node(data,node)
    
    def get_min(self):
        
        if self.node:
            return self.get_min_value(self.root)
    
    def get_min_value(self,node):
        
        if node.left_node:
            self.get_min_value(node.left_node)
        
        return node.value

    def get_max(self):
        if self.node:
            return self.get_max_value(self.root)
    
    def get_max_value(self,node):

        if node.right_node:
            self.get_max_value(node.right_node)

        return node.value
    
    def traverse(self):
       
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self,node):
        


        
