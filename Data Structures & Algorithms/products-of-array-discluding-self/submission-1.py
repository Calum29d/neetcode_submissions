class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums) #include the prefix inside the array
        suffix = 1 #set up this for when we multiply the ans and suffix together
        

        for i in range(1,len(nums)): 
            ans[i] = ans[i-1] * nums[i-1] #

        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * suffix
            suffix *= nums[i]
            
        return ans







                


        