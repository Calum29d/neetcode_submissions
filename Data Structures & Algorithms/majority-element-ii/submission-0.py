class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # sort nums
        # loop through the sorted array counting the occurence of each element
        # if > n / 3 we then can add it to res

        nums.sort()
        res = []

        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if (j - i) > len(nums) // 3:
                res.append(nums[i])
            
            i = j
        
        return res

        #O(nlogn)
        #O(1)
        

        