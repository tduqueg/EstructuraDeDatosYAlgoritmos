class Node:

    def __init__(self,data,parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

class AVLTree:

    def __init__(self):
        #Podemos acceder exclusivamente al nodo raíz
        self.root = None
    
    def remove(self,data):
        
        if self.root:
            self.remove_node(data, self.root)

    def insert(self,data):

        if self.root is None:
            self.root = Node(data, None)
        
        else:
            self.insert_node(data,self.root)
    
    def insert_node(self,data,node):

        # Debemos considerar el subarbol izquierdo
        if data < node.data:
            #Debemos revisar si el nodo izquierdo está vacío
            if node.left_node:
                self.insert_node(data,node.left_node)
            else:
                node.left_node = Node(data,node)
                node.height = max(self.calc_height(node.left_node),self.calc_height(node.right_node))+1
        #Debemos considerar el árbol derecho
        else:
            #Debemos revisar si el nodo derecho está vacío
            if node.right_node:
                self.insert_node(data,node.right_node)
            else:
                node.right_node = Node(data,node)
                node.height = max(self.calc_height(node.left_node),self.calc_height(node.right_node))+1
        
        #Después de cada insersión debemos considerar si las propiedades de un árbol AVL se están cumpliendo
        self.handle_violation(node)
    
    def remove_node(self,data,node):

        if node is None:
            return
        
        if data < node.data:
            self.remove_node(data,node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        #Encontramos el nodo que queremos eliminar
        else:
            
            #Caso 1, el nodo es un nodo hoja
            if node.left_node is None and node.right_node is None:
                print("Eliminando nodo hoja... %d" % node.data)
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                
                if parent is None:
                    self.root = None
                
                del node

                self.handle_violation(parent)

            #Caso 2, si el nodo tiene un solo nodo hijo
            elif node.left_node is None and node.right_node is not None:
                print("Eliminando un nodo con un solo hijo derecho... %d" % node.data)
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                
                else:
                    self.root = node.right_node
                
                node.right_node.parent = parent

                del node

                self.handle_violation(parent)
            
            elif node.right_node is None and node.left_node is not None:
                print("Eliminando un nodo con un solo hijo izquierdo... %d" % node.data)
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                
                else:
                    self.root = node.left_node
                
                node.left_node.parent = parent

                del node

                self.handle_violation(parent)

            #Caso 3, el nodo tiene 2 nodos hijos
            else:
                print("Eliminando un nodo con dos hijos... %d" % node.data)

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data,predecessor)

    def get_predecessor(self,node):

        if node.right_node:
            return self.get_predecessor(node.right_node)
        
        return node
    
    def handle_violation(self,node):
        
        #Revisa los nodos desde el nodo que modificamos hasta el nodo raíz
        while node is not None:
            node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))+1

            self.violation_helper(node)
            #Cada vez que hacemos una rotación puede pasar que se deban hacer más rotaciones en otra parte del árbol
            node = node.parent

    #Revisa si el subarbol est´á balanceado con el nodo raíz = nodo
    def violation_helper(self,node):

        balance = self.calculate_balance(node)

        #Sabemos que si el balance es mayor a uno el árbol es más pesado a la izquierda pero puede tener subarboles pesados a la derecha
        if balance > 1 :
            
            if self.calculate_balance(node.left_node) < 0:
                
                self.rotate_left(node.left_node)

            self.rotate_right(node)
        
        #Sabemos que si el balances es menor a menos uno el árbol es más pesado a la derecha, pero puede tener subarboles pesados a la izquierda
        if balance < -1:
            
            if self.calculate_balance(node.right_node) > 0:
                
                self.rotate_right(node.right_node)
            
            self.rotate_left(node)

     
    def calc_height(self, node):

        if node is None:
            return -1

        return node.height
    
    def calculate_balance(self, node):

        if node is None:
            return 0
        
        return self.calc_height(node.left_node) - self.calc_height(node.right_node)
    
    #Su complejidad es de O(1)
    def rotate_right(self, node):
        
        print("Rotando a la derecha en el nodo ", node.data)
        
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
        
        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) +1
        temp_left_node.height = max(self.calc_height(temp_left_node.left_node),self.calc_height(temp_left_node.right_node)) +1

    #Su complejidad es de O(1)
    def rotate_left(self, node):
        
        print("Rotando a la izquierda en el nodo ", node.data)

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

        node.height = max(self.calc_height(node.left_node),self.calc_height(node.right_node)) +1
        temp_right_node.height = max(self.calc_height(temp_right_node.left_node),self.calc_height(temp_right_node.right_node))+1

    def traverse(self):

        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self,node):

        if node.left_node:
            self.traverse_in_order(node.left_node)

        l = ''
        r = ''
        p = ''

        if node.left_node is not None:

            l = node.left_node.data
        
        else:
            
            l = 'NULL'

        if node.right_node is not None:

            r = node.right_node.data
        
        else:

            r = 'NULL'
        
        if node.parent is not None:

            p = node.parent.data

        else:

            p = 'NULL'
        
        print("%s left: %s right: %s parent: %s height: %s" % (node.data, l, r, p, node.height))

        if node.right_node:

            self.traverse_in_order(node.right_node)

if __name__ == '__main__':

    avl = AVLTree()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(5)
    avl.insert(10)
    avl.insert(4)
    avl.insert(-2)
    avl.insert(9)
    avl.insert(30)
    avl.insert(23)
    avl.insert(98)
    avl.traverse()





        






                

            

                 


            






