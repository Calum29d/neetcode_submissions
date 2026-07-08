class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #store that the when we get to the last index/space after the last word then we already know
        #that will return true as we have gotten to the end of the string
        #we will store which index's return true or false in this cache to stop repeated work
        memo = {len(s):True}

        def dfs(i):
            #base case
            if i in memo:
                return memo[i]
            
            #try every word
            for word in wordDict:
                #check if word matches, if so start see if the rest of the word can be broken up and return true if so
                if word == s[i : i + len(word)]:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            
            #if we never return True then we know the word cant be broken up
            memo[i] = False
            return False
        
        return dfs(0)

        #Time complexity O(n * w * l) where n is length of string, w is num of words and l is max length of word in dict
        #Space complexity O(n) where n is the length of the string as memo can store boolean per position and O(n) for stack call
        #so overall O(n) space
            

                
                



        