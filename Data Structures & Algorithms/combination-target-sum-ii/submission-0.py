class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        candidates.sort()

        def dfs(i,curSum):
            # Base case
            if curSum == target:
                res.append(subset.copy())
                return

            if curSum > target or i >= len(candidates):
                return
            
            # include current cadidate
            subset.append(candidates[i])
            dfs(i + 1, curSum + candidates[i])

            # exclude current candidate
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curSum)
        
        dfs(0, 0)

        return res
            
            
        
        