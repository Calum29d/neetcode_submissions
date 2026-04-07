class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        #brute force method test
        
        word1 = list(s)
        word2 = list(t)

        if sorted(word1) == sorted(word2):
            return True
        else:
            return False
            #this method should be O(n + m) time
            #but this is also O(n + m) space but it needs to be O(1)
            """
            
        word1Freq = {}
        word2Freq = {}

        #2 for loops make O(n + m) time
        #im not too sure about making 2 hashTables, being O(1) space as the string length isnt really fixed
        for letter in s:
            word1Freq[letter] = word1Freq.get(letter, 0) + 1 #will add 1 to the current letter freqency
        
        for letter in t:
            word2Freq[letter] = word2Freq.get(letter, 0) + 1 
        
        if word1Freq == word2Freq:
            return True
        else:
            return False

    


    
    
        


