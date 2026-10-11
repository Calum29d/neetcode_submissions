class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1, 1, 1, 1] -> [1, 2, 4]
        res = [1] * len(nums)
        suffix = 1

        #set up prefix
        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * suffix
            suffix *= nums[i]
        
        return res



        