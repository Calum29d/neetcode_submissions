class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # 2 decisions per call, open a bracket or close a bracket
        # but i cant close a bracket unless there is already an opened  bracket to be closed 
        # i can probably keep count of open and close brackets
        
        res = []

        def backTrack(curString, openCount, closeCount):
            # base case if the string has reached n parentheses
            if len(curString) == 2*n:
                res.append(curString)
            
            # if we can still open brackets
            if openCount < n:
                backTrack(curString + "(", openCount + 1, closeCount)
            # if we can still close brackets
            if closeCount < openCount:
                backTrack(curString + ")", openCount, closeCount + 1)
        
        backTrack("", 0 ,0)
        return res

        # Time: No idea
        # Space: O(n)


        