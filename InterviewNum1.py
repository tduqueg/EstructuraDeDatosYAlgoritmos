
def reverse(nums):
    
    start_index = 0

    end_index = len(nums)-1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index +=1
        end_index -= 1

if __name__ == '__main__':
    n = [4,65,73,2,2,4,6,61,14,6,644,4,35,235,4,345,342,325,45,31,5,12,345,2,67,235,34,46,82,23,49,9,3,2,3,6,4,234,567,345,72,3,2345,6712454]
    reverse(n)
    print(n)