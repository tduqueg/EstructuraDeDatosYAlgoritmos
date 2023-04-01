import random

ITEMS_IN_BUCKET = 10

class RadixSort:



    def __init__(self,data):

        self.data = data
    
    def get_digits(self):

        return len(str(max(self.data)))
    
    def sort(self):

        for digit in range(self.get_digits()):
            
            self.counting_sort(digit)

    def counting_sort(self,d):

        count_array = [[] for _ in range(ITEMS_IN_BUCKET)]

        #O(n) complejidad
        for num in self.data:
            
            #Calculamos el índice del bucket
            index = (num // (10 ** d)) % 10
            count_array[index].append(num)

        #Tenemos que considerar todos los ítems de la lista
        z = 0
        for i in range(len(count_array)):

            while len(count_array[i]):
                
                self.data[z] = count_array[i].pop(0)
                z += 1

if __name__ == "__main__":
    
    data = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1,35,3673,73,37,435,235,87,384,36437 ,53834,3487,5438,467,3473462346,28,24724,5324,248,427,23452,3213,72487,22,56223,47346]
    random.shuffle(data)
    radix = RadixSort(data)
    radix.sort()
    print(radix.data)




