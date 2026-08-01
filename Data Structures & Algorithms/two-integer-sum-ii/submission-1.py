class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0 , len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum == target:
                return [1 + l, 1 + r]
            
            #if sum is greater than target we know to move the r pointer left
            if currSum > target:
                r -= 1
            
            else:
                l += 1
        
        return [] #although this problem states that there will always be a solution so there isnt really a need for this


        