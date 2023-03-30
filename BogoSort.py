import random

class BogoSort:

    def __init__(self,nums):

        self.nums = nums
    
    def is_sorted(self):

        for i in range(len(self.nums)-1):

            if self.nums[i] > self.nums[i+1]:

                return False
        
        return True
    
    def sort(self):
        x=0
        while not self.is_sorted():
            
            print('Mezclando por %d vez...' % x)
            self.shuffle()
            x +=1
    
    #Fisher-Yates shuffle, generamos una permutación nueva en O(n)
    def shuffle(self):

        for i in range(len(self.nums)-2, -1, -1):

            j = random.randint(0, i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

if __name__ == '__main__':
    algorithm = BogoSort([1,32,56,2,24,3,-1])
    algorithm.sort()
    print(algorithm.nums)

        



