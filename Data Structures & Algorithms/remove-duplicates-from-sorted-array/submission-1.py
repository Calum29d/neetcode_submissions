class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]: # if element is not in group anymore / is unique
                nums[l] = nums[r]
                l += 1 # get ready to place next unique element
        
        return l
    
        # O(n) time O(1) space


                
        