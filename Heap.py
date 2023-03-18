CAPACITY = 10

#Definimos el max Heap
class Heap:

    def __init__(self):
        #Este es la cantidad actual de items en la estructura de datos
        self.heap_size = 0
        self.heap = [0]*CAPACITY

    #La complejidad de la inserción es de O(1)
    def insert(self,item):

        #Cuando la estructura de datos está llena
        if self.heap_size == CAPACITY:
            return
        
        self.heap[self.heap_size] = item
        self.heap_size += 1

        #Revisamos que se cumplan las propiedades del Heap
        self.fix_up(self.heap_size-1)

    #Empieza con el nodo que insertamos hasta el nodo raíz en el peor de los casos
    #Comparamos los valores para saber si hacemos el cambio o no
    #Su complejidad de tiempo de ejecuci´ón es de O(logN) 
    def fix_up(self,index):

        parent_index = (index-1)//2

        #Consideramos todos los items arriba de este nodo hasta llegar al nodo raiz
        #si las propiedades del Heap son violadas cambiamos el hijo por el padre
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    #Devuelve el item maximo con una complejidad de O(1)
    def get_max(self):
        return self.heap[0]
    
    #Devuelve el número máximo y lo elimina tambien
    #Elimina el nodo raíz
    #Tiene una complejidad de O(logn)
    def poll(self):

        max_item = self.get_max()

        #Cambiamos el nodo raíz con el último item y realizamos "Heapify"
        self.heap[0],self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
        self.heap_size -= 1

        #Nos aseguramos que el heap este Heapify
        #Heapify tiene una complejidad de O(logn)
        self.fix_down(0)

        return max_item
    
    #Empieza en el nodo raíz para abajo hasta que las propiedades del heap no se violen
    #Su complejidad de tiempo de ejecución es de O(logN)
    def fix_down(self,index):

        left_index = 2 * index +1
        right_index = 2 * index +2

        #En el max Heap los padres siempre serán mayores a los hijos
        largest_index = index

        #Buscamos el más grande(padre o nodo izquierdo)
        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index
        
        #Si el hijo derecho es mayore que el hijo izquierdo entonces el numero más grande es el hijo derecho
        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        #Si el padre es mayor que el hijo entonces cumple las propiedades del heap y termina la recursividad
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    
    def heap_sort(self):

        #como consideramos n elementos y la complejidad de cada elemento es O(logN) entonces
        #la complejidad de heap sort es de O(NlogN)
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)

if __name__ == '__main__':
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    heap.heap_sort()
    print(heap.heap)





