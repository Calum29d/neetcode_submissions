class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l, r = i, i
            #handle odd strings
            #loop while we have found a palindrome, and increment each time as each substring of a palindrome is also a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

            
            #handle even strings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            

        return count

        #O(n^2) time and O(1) space
        
        