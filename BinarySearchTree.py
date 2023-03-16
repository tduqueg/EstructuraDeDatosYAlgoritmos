
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
        
        if self.root:
            return self.get_min_value(self.root)
    
    def get_min_value(self,node):
        
        if node.left_node:
            return self.get_min_value(node.left_node)
        
        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)
    
    def get_max_value(self,node):

        if node.right_node:
            return self.get_max_value(node.right_node)

        return node.data
    
    def traverse(self):
       
        if self.root:
            self.traverse_in_order(self.root)

    #Tiene una complejidad de O(n) debido a que debemos visitar cada uno de los ítems
    def traverse_in_order(self,node):
        
        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(9)
    bst.insert(20)
    bst.insert(32)
    bst.insert(-2)
    bst.insert(3)
    bst.insert(200)
    bst.insert(-50)
    bst.insert(69)
    bst.insert(-96)
    bst.traverse()
    print("Valor Máximo: %d" % bst.get_max())
    print("Valor Minimo: %d" % bst.get_min())
    
        



        
