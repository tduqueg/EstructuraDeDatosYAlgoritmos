
class CountingSort:

    def __init__(self,data):

        self.data = data
        self.count_array = [0 for _ in range(max(data)-min(data)+1)]

    def sort(self):

        #Primero consideramos todos los ítems de la lista en O(n)
        for i in range(len(self.data)):

            self.count_array[self.data[i]-min(self.data)] += 1 

        #Debemos considerar el count_array en O(k)
        z = 0
        
        for i in range(min(self.data),max(self.data)+1):

            while self.count_array[i-min(self.data)]:

                self.data[z] = i
                z += 1
                self.count_array[i-min(self.data)] -= 1

if __name__ == '__main__':

    n = [1,56,2,5,7,2,1,6,7,34,2,6,87,98,6,478,9,43,9,0,-4,-3,-6,8,-2]
    counting = CountingSort(n)
    counting.sort()
    print(n)





             
