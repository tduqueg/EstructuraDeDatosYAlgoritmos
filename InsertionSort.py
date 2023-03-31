
def insertion_sort(nums):

    for i in range(len(nums)):

        j = i

        #Tenemos que comparar los ítems anteriores al que vamos a organizar
        #En el peor de los casos consideramos todos los ítems previos hasta que j = 0
        while j > 0 and nums[j-1] > nums[j]:
            
            #Cambiamos los items
            nums[j-1],nums[j] = nums[j],nums[j-1]
            j -= 1

if __name__ == "__main__":

    n = [6,3,26,2,7,8,323,4,7,83,2,4,4,678,89,3,42,41,68,65,8,56,45254378,57,845,3465]
    insertion_sort(n)
    print(n)


