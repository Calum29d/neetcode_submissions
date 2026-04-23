class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        currChars = set()
        maxLength = 0

        for r in range(len(s)):
            while s[r] in currChars: #makes the window smaller from the left if the right char is in the window, will continue looping until all dupes are gone
                currChars.remove(s[l])
                l += 1
            
            currChars.add(s[r]) #add the current char to the window
            maxLength = max(maxLength, r - l + 1) #calculates the length of the window

        return maxLength


    

        
            


        
