class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combination, total):
            if total == target:
                res.append(combination.copy()) #make a copy as when the combination gets updated res also gets updated so have to make a new list
                return
            #if we have tried every number or the total is not going to equal the target
            if i >= len(nums) or total > target:
                return
            
            #add the current num to the combination
            combination.append(nums[i])
            #allow for the same num to be used
            dfs(i, combination, total + nums[i])
            #backtracking step, take back the decision we just made
            combination.pop()
            #and then try nums without including num[i]
            dfs(i + 1, combination, total)

        dfs(0, [], 0)

        return res
        