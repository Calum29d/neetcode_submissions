class Solution:
    def rob(self, nums: List[int]) -> int:

        def simpleRob(nums):

            rob1, rob2 = 0, 0

            for n in nums:
                #decide whether its better to rob the current house or skip it
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        #skip the first house and the last house and return whatever way or robbing is greater
        return max(nums[0], simpleRob(nums[1:]), simpleRob(nums[:-1]))

        