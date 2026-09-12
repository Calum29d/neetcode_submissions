class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        
        return max(freqMap.items(), key = lambda x: x[1])[0]
        