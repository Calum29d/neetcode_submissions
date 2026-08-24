class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]

        res = []
        subset = []

        def dfs(i):
            # Base case: if we are out of bounds
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision to include cur index
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack / decide not to include cur index
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

        # O(n * 2^n) 2 decisions per call for up to n elements



        