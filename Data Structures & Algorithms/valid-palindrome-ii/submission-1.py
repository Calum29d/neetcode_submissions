class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (isPalin(l + 1, r) or isPalin(l, r - 1)) # check if the rest of the string is a palin from both choices of removal 
            l += 1
            r -= 1

        return True

        # O(n) time O(1) space

        


        