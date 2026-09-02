class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for num in nums:
            if num - 1 not in numSet: # if its start of a sequence
                curSeq = 1
                
                while num + curSeq in numSet:
                    curSeq += 1
                longestSeq = max(longestSeq, curSeq)
        
        return longestSeq




        