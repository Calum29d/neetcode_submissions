class Solution:
    def sortColors(self, nums: List[int]) -> None:

        colourCount = [0] * 3

        for num in nums:
            colourCount[num] += 1
        
        index = 0
        for i in range(3):
            while colourCount[i]:
                nums[index] = i
                index += 1
                colourCount[i] -= 1
        
        # O(n) time O(1) space

        