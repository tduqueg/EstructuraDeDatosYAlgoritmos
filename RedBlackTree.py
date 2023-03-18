class Color:

    RED = 1
    BLACK = 2

class Node:

    def __init__(self,data,parent=None, color = Color.RED):

        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.color = color

class RedBlackTree:

    def __init__(self):
        
        self.root = None

    def insert(self,data):
        
        if self.root is None:
            self.root = Node(data)
            self.settle_violation(self.root)

        else:
            self.insert_node(data, self.root)

    def insert_node(self,data, node):

        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                self.settle_violation(node.left_node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                self.settle_violation(node.right_node)

    def settle_violation(self, node):

        while node != self.root and self.is_red(node) and self.is_red(node.parent):

            parent_node = node.parent
            grand_parent_node = parent_node.parent

            # El padre es un nodo hijo en la izquierda del nodo abuelo
            if parent_node == grand_parent_node.left_node:
                uncle = grand_parent_node.right_node

                # Caso 1 y caso 4 RECOLOREAR
                if uncle and self.is_red(uncle):
                    print("Recoloreando nodo %s a ROJO" % grand_parent_node.data)
                    grand_parent_node.color = Color.RED
                    print("Recoloreando nodo %s a Negro" % parent_node.data)
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                
                else:
                    #Caso 2 el nodo tio es negro y el nodo es un nodo hijo izquierdo
                    if node == parent_node.right_node:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    
                    #Caso 3 se rota el nodo abuelo, además en nodo padre y el nodo abuelo cambian de color
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print("Recoloreando nodo %s a NEGRO" % parent_node.data)
                    print("Recoloreando nodo %s a ROJO" % grand_parent_node.data)
                    self.rotate_right(grand_parent_node)
            
            else:
                
                uncle = grand_parent_node.left_node

                if uncle and self.is_red(uncle):
                    
                    #Caso 1 y caso 4
                    print("Recoloreando nodo %s a ROJO" % grand_parent_node.data)
                    grand_parent_node.color = Color.RED
                    print("Recoloreando nodo %s a NEGRO" % parent_node.data)
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                
                else:

                    #Caso 2 si el nodo tio es negro y el nodo es un hijo derecho
                    if node == parent_node.left_node:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    
                    #caso 3
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print("Recoloreando nodo %s a NEGRO" % parent_node.data)
                    print("Recoloreando nodo %s a ROJO" % grand_parent_node.data)
                    self.rotate_left(grand_parent_node)
            
        if self.is_red(self.root):
            print("Recoloreando el nodo raiz a negro...")
            self.root.color = Color.BLACK
            
                    





    def is_red(self, node):
        
        if node is None:

            return False

        return node.color == Color.RED

    def traverse(self):
        
        if self.root:
            self.in_order_traversal(self.root)
    
    def in_order_traversal(self, node):

        if node.left_node:
            self.in_order_traversal(node.left_node)
        
        print(node.data)

        if node.right_node:
            self.in_order_traversal(node.right_node)
    
    def rotate_right(self, node):

        print("Rotando a la derecha el nodo ", node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            
            t.parent = node
        
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node
        
        if node == self.root:
            self.root = temp_left_node
    
    def rotate_left(self, node):

        print("Rotando a la izquierda el nodo ", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            
            t.parent = node
        
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node
        
        if node == self.root:

            self.root = temp_right_node

if __name__ == '__main__':

    rbt = RedBlackTree()
    rbt.insert(32)
    rbt.insert(10)
    rbt.insert(55)
    rbt.insert(1)
    rbt.insert(19)
    rbt.insert(79)
    rbt.insert(16)
    rbt.insert(23)
    rbt.insert(12)

    rbt.traverse()






