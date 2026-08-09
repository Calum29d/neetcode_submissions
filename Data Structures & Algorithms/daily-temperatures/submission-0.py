class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair of [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #until we find a day that has greater temp than the last
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            
            #keep on adding days to the stack
            stack.append([t, i])
            
        return res

        #O(n) time and space
                

        