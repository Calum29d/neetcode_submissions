class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, windowTotal = 0, 0
        res = float("inf") 

        for r in range(len(nums)):
            windowTotal += nums[r]

            while windowTotal >= target:
                res = min((r - l) + 1, res)
                windowTotal -= nums[l]
                l += 1
        
        return 0 if res == float("inf") else res

        #O(n) time O(1) space