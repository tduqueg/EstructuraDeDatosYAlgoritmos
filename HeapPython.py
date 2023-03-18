import heapq

#Es una implementación de un min Heap

nums = [4,7,3,-2,1,0]
heap = []
heap1 = [9,8,7,6,5,4]

#Con la libreria heapq se puede realizar de la siguiente manera
# heapq.heapify(nums)

# print(nums)

#También se puede realizar de está forma con la misma libreria
for value in nums:
    heapq.heappush(heap, value)

print(heap)
def is_min_heap(heap):
    
    #No hay necesidad de revisar los nodos hojas
    num_items = (len(heap) - 2)//2
    
    #Los padres deben ser menores a los hijos
    for i in range(num_items):
        if heap[i] > heap[(2*i+1)] or heap[i] > heap[(2*i+2)]:
            return False
        return True

print(is_min_heap(heap))

def min_to_max_heap(heap):

    #Revisamos que sea un min Heap
    if is_min_heap(heap) == True:

    #Lo convertimos en un max Heap
        heapq._heapify_max(heap)
        return heap
    
    #Si no es un min Heap lo convertimos en un min Heap con heapify
    heapq.heapify(heap)
    min_to_max_heap(heap)

print(min_to_max_heap(heap))


#Así podemos sacar el ítem con el menor valor en orden
while heap:
    print(heapq.heappop(heap))



    
    



