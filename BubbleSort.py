
class BubbleSort:

    def __init__(self,nums):

        self.nums = nums
        
    
    def sort(self):

        for i in range(len(self.nums)-1):

            for j in range(len(self.nums)-i-1):

                if self.nums[j] > self.nums[j+1]:

                    
                    self.swap(j,j+1)




    def swap(self,i,j):

        self.nums[i],self.nums[j] = self.nums[j],self.nums[i]

if __name__ == "__main__":

    algorithm = BubbleSort([1,4,32,5,11,26,14,345,324,23,43,235,462,536,24,26,3,534,12,5,76547,2342,57,4,32,42,6,78,35,72])
    algorithm.sort()
    print(algorithm.nums)