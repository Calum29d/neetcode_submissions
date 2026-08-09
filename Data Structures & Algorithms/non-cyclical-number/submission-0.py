class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            nextNum = 0

            for digit in str(n):
                nextNum += int(digit) ** 2
            
            n = nextNum
            
        return True

        #O(logn) time O(n) space
        