class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

            if freqMap[num] > len(nums) // 2: # if its the majority number
                return num
        

        