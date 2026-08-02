class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #means no possible permuatation
        if len(s1) > len(s2):
            return False
        
        s1Freq = {}
        s2Freq = {}

        #get freq of s1 and also sets up the window to be the size of s1
        for i in range(len(s1)):
            s1Freq[s1[i]] = s1Freq.get(s1[i], 0) + 1
            s2Freq[s2[i]] = s2Freq.get(s2[i], 0) + 1
        
        #check if they are equal before checking the rest of s2
        if s1Freq == s2Freq:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            #move window right by adding new char
            s2Freq[s2[r]] = s2Freq.get(s2[r], 0) + 1

            #then remove the left most char to finish moving the window
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]
            l += 1

            if s1Freq == s2Freq:
                return True

        return False

        #O(n) time and O(26) space -> O(1) space
            
        