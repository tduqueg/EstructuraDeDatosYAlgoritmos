
def merge_sort(nums):

    #Como es un acercamiento dividir y conquistar, depende de la 
    #recursión 
    if len(nums) ==1:
        return
    
    #Aquí hacemos la división
    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    #Aquí hacemos la fase de "conquista"
    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        
        if left_half[i] < right_half[j]:

            nums[k] = left_half[i]
            i += 1
        else:

            nums[k] = right_half[j]
            j += 1
            
        k += 1 
    
    #Después de esto pueden haber ítems adicionales en la izquierda o en la derecha
    while i < len(left_half):
        
        nums[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        
        nums[k] = right_half[j]
        j += 1 
        k += 1

if __name__ == '__main__':

    n = [1,2,51,4,76,1,4,1,6,72,12,3,5,27,23,3,41,2,7,872,4,26,28,21]
    merge_sort(n)
    print(n)