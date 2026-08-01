class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = [0] * len(height)  #store the max height from the current positions left
        maxRight = [0] * len(height) #store the max height from the current positions right
        waterTrapped = 0

        leftMax = 0
        for i in range(len(height)):

            leftMax = max(leftMax, height[i])
            maxLeft[i] = leftMax
        
        rightMax = 0
        for i in range(len(height) - 1, -1, -1):

            rightMax= max(rightMax, height[i])
            maxRight[i] = rightMax
        
        #now calcuate the trapped water
        for i in range(len(height)):
            waterInPosition = min(maxLeft[i], maxRight[i]) - height[i]

            if waterInPosition > 0:
                waterTrapped += waterInPosition
        
        return waterTrapped
    
    #O(n) time and space

            

    


        
        