
def selection_sort(nums):

    #realizamos n-1 iteraciones
    #por lo que la complejidad es de
    #n - 1 x O(n) = O(n x n) = O(n^2)
    for i in range(len(nums)-1):

        #Hacemos una busqueda lineal simple y el index almacena 
        #el ítem mínimo
        index = i

        #Este es la busqueda lineal con complejidad de O(n)
        for j in range(i,len(nums)):

            if nums[j] < nums[index]:

                index = j
        
        #Luego hacemos un cambio del ítem mínimo con el ítem
        #a toda la izquierda
        if index != i:

            nums[index], nums[i] = nums[i],nums[index]

if __name__ == '__main__':
    
    n = [6,42,5,7,2,2,5,7,2,23,4,5,7,5,3,78,567,456,8,43,2,246,7,8]
    selection_sort(n)
    print(n)
    

