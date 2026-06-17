class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):

            #shift the one step position back and two back
            one, two = one + two, one

        return one

#O(n) time and O(1) space, this is the true DP approach 
