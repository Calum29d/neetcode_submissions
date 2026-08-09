class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #tuple (index, height)

        for i, h in enumerate(heights):
            #set the start pos used to set the max width
            startPos = i

            #loop while the stack isnt empty and the heights arent stricly increasing
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                startPos = index
            
            stack.append((startPos, h))

        #calculate leftover rectangles
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

        #O(n) time and space
        
        