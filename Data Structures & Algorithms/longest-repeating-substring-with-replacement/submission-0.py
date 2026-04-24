class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        maxLen = 0
        count = {}

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            #loop only while the current window is invalid
            while r - l + 1 - self.findMaxFreq(count) > k: 
                count[s[l]] -= 1 #remove 1 from the left pointers char as its not in window anymore
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen
        
    #use this function to easily find the max freq 
    def findMaxFreq(self, count):
        maxFreq = 0

        for val in count.values():
            if val > maxFreq:
                maxFreq = val
        return maxFreq

        #O(26*n) time which is linear, and O(m) space where is the num of unique chars in the string
        

            
                

        