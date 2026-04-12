class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    ans[i] *= nums[j]
        return ans

        #this is also a O(n^2) time solution, i tried on my first submission to make it O(n) but it ended up 
        #O(n^2) but this is just a much shorter way of doing it for O(n^2)
        