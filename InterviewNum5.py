def problema_de_la_bandera(nums,pivot = 1):
    i = 0
    j = 0
    k = len(nums)-1

    while j <= k:
        if nums[j] < pivot:
            swap(nums, i , j)
            i += 1
            j += 1
        elif nums[j] > pivot:
            swap(nums, j,k)
            k -= 1
        else:
            j += 1
    return(nums)

def swap(nums,index1,index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

if __name__ == '__main__':
    print(problema_de_la_bandera([1,1,1,1,1,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,1,2,1,2,1,0,1]))