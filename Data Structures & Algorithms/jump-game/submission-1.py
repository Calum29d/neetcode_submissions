class Solution:
    def canJump(self, nums: List[int]) -> bool:

        #greedy approach, got the brute force way DP method but would never think of this
        #O(n) time O(1) space

        goal = len(nums) -1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        #return whether the goal has reached the start or not
        return goal == 0
        