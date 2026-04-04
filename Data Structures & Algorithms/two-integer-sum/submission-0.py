class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            numberToFind = target - nums[i]

            if numberToFind in hashmap:
                j = hashmap[numberToFind]
                return sorted([i,j])
            else:
                hashmap[nums[i]] = i
        
            
        