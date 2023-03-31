
def shell_sort(nums):

    gap = len(nums)//2

    #Esto es lo que diferencia el ShellSort de Insertion Sort
    while gap > 0:

        for i in range(gap, len(nums)):
            
            j = i

            while j >= gap and nums[j-gap] > nums[j]:

                nums[j], nums[j-gap] = nums[j-gap], nums[j]

        gap = gap // 2

if __name__ == '__main__':

    n = [23,1,54,736,23455,34,2,47,32,34,234,5,12,34]
    shell_sort(n)
    print(n)