class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
    
        maxVol = 0 #vol = width * min(left height, right height)

        while l < r:
            currVol = (r-l) * min(heights[l], heights[r])
            
            #only increment/decrement the smaller bar
            if heights[l] < heights[r]:
                l += 1  
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
            if currVol > maxVol:
                maxVol = currVol

        return maxVol

        #time O(n) space O(1) this one was a lot easier than 3Sum


            

            
            
            

        

                

        