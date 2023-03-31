
class QuickSort:

    def __init__(self,data):

        self.data = data

    def sort(self):

        self.quick_sort(0, len(self.data)-1)

    #Low es el índice del primer ítem y high el del último
    def quick_sort(self,low, high):

        if low >= high:
            return
        
        pivot_index = self.partition(low,high)
        #Llamamos la función recursivamente con el subarray izquierdo
        self.quick_sort(low, pivot_index-1)
        #Llamamos la función recursivamente con el subarray derecho
        self.quick_sort(pivot_index+1, high)

    #O(n)
    def partition(self,low,high):

        #El pivote en este caso será el número de la mitad
        pivot_index = (low + high) // 2

        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        #Consideramos todos los ítems y los comparamos con el pivote

        for j in range(low, high):

            if self.data[j] <= self.data[high]:

                self.data[low], self.data[j] = self.data[j], self.data[low]
                low += 1
        
        self.data[low], self.data[high] = self.data[high], self.data[low]

        return low

if __name__ == '__main__':
    x = [1,52,0,42,903,94,235,92,493,434]
    algorithm = QuickSort(x)
    algorithm.sort()
    print(x)

