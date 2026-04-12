class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums) #initalise 1's in the array to so the first number multiplied is just itself
        

        for i in range(len(nums)): # loop for each number in the array
            for j in range(i): # loop up to just before the index of the number we are currently processing
                prefix[i] = nums[j] * prefix[i] # multiply all numbers before the num we are processing
            for k in range(len(nums)-1, i, -1):
                suffix[i] = nums[k] * suffix[i] # multiply all numbers after the num we are processing
            
            ans.append(prefix[i] * suffix[i]) #multiply the 2 numbers we calculated 
        return ans

        #first medium i havent had to watch a video for
        #im not entirely sure if this is O(n) or not as there are 3 loops, i think it may be O(n^2) time 
        #as the 2 half loops add up to n




                


        