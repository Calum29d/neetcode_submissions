class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0 # 0 represents
        white = 0 # 1 represents
        blue = 0 # 2 represents

        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            elif num == 2:
                blue += 1
        
        for i in range(red):
            nums[i] = 0
        for i in range(red, red + white):
            nums[i] = 1
        for i in range(red + white, red + white + blue):
            nums[i] = 2
        