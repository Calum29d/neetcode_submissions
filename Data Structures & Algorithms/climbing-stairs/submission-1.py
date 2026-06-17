class Solution:
    def climbStairs(self, n: int) -> int:
        #store previously cacluated results
        memo = {}
        

        def dfs(remain):
            if remain == 0:
                return 1
            
            if remain < 0:
                return 0

            #dont calculate the a result we have already calculated
            if remain in memo:
                return memo[remain]

            memo[remain] = dfs(remain - 1) + dfs(remain - 2)

            return memo[remain]
        return dfs(n)

        #O(n) time and space but its not DP, which i have no idea how to do
        