class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}


        def dfs(i):
            #if we have calculated LIS from curr position
            if i in memo:
                return memo[i]
            
            LISFromCurr = 1

            for j in range(i + 1, len(nums)):
                #decide whether to include the next num
                if nums[i] < nums[j]:
                    LISFromCurr = max(LISFromCurr, 1 + dfs(j))
            
            memo[i] = LISFromCurr
            return LISFromCurr
        
        #return the greatest LIS length
        return max(dfs(i) for i in range(len(nums)))
        
        
            