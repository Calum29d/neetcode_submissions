class Solution:
    def numDecodings(self, s: str) -> int:
        #top down DP method O(n) time and space due to memoization
        #cache previous calculated results
        memo = [-1 for i in range(len(s))]

        def helper(curr, s, memo):
            if curr == 0:
                if s[0] == "0":
                    memo[curr] = 0
                    return 0
                else:
                    memo[curr] = 1
                    return 1
            
            if curr == -1:
                return 1

            if memo[curr] != -1:
                return memo[curr]

            if s[curr] == "0":
                if s[curr - 1] == "1" or s[curr - 1] == "2":
                    memo[curr] = helper(curr - 2, s, memo)
                    return memo[curr]
                else:
                    memo[curr] = 0
                    return memo[curr]
            
            ways = 0
            if (s[curr-1] == "1") or (s[curr-1] == "2" and int(s[curr]) < 7):
                ways = helper(curr-1, s, memo) + helper(curr-2, s, memo)
            else:
                ways = helper(curr-1, s, memo)
            
            memo[curr] = ways
            return ways

        return helper(len(s)-1, s, memo)
        
        