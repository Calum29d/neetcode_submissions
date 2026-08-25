class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curPerm = set()

        def dfs(curNum, perm):

            curPerm.add(curNum)
            perm.append(curNum)

            # Base case
            if len(perm) == len(nums):
                res.append(perm.copy())
            else:
                for num in nums:
                    if num not in curPerm:
                        dfs(num,perm)
                
            curPerm.remove(curNum)
            perm.pop()
            
            

        # start recursion on each 'decision' we can make
        for num in nums:
            dfs(num, [])
        
        return res

        # Time: O(n * n!) as we take a copy of the perm array and there are n! permutations
        # Space: O(n) as the set can have up to n elements and call stack up to n, but space is less efficent if you are counting the res stored

            

            

        