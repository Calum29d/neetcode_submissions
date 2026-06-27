class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            #handle odd length palindromes first
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #if length of current substring palin is greater than last found one then update
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1
            
            #handle the even length palindromes by setting the middle as 2 chars
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1
        
        return res

        #O(n^2) time and O(1) space
        