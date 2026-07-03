class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #kadanes algorithm O(n) time O(1) space

        res = nums[0]
        maxEnd = res

        for i in range(1,len(nums)):
            
            #decide whether to extend the current subarry or start new sum from curr
            maxEnd = max(maxEnd + nums[i], nums[i])

            res = max(maxEnd, res)

        return res

        