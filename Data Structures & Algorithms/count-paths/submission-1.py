class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #memo will keep coordinate positons and how many unique paths come from that position
        memo = {}

        def dfs(y, x):
            #check if num of unique paths from this position has already been calculated
            if (y, x) in memo:
                return memo[(y, x)]
            
            #out of bounds
            if y == m or x == n:
                return 0
            
            #goal reached
            if y == m-1 and x == n-1:
                return 1
            
            paths = dfs(y + 1, x) + dfs(y, x + 1)
            
            memo[(y, x)] = paths

            return paths
        
        return dfs(0, 0)

        #O(m * n) time and O(m * n) space

            

            
            