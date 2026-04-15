class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        ans = []


        if len(nums) == 1:
            return 1
        

        for i in range(len(nums)):
            length = 1
            numToFind = nums[i] + 1
            while numToFind in setNums:
                length += 1
                numToFind += 1
            ans.append(length)

        if len(ans) == 0:
            return 0
        else:
            return max(ans)
        #this is a pretty bad solution, but O(n^2) time and O(n) space 
     
            



        