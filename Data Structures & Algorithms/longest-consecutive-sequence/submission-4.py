class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxLength = 0

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            length = 1
            numToFind = nums[i] + 1
            if nums[i] - 1 not in setNums: # this line makes it O(n) as it checks if the number is the start of a sequence
                while numToFind in setNums:
                    length += 1
                    numToFind += 1
            if maxLength < length:
                maxLength = length

        return maxLength

            #this is the o(n) time and space solution, I was actually pretty close with this from my first attempt, just a little hint from GPT and i realised
            #check if the number was part of a sequence or the start of one.
     
            



        