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
                #check if word matches, if so start dfs on new postion in string and try every word
                if word == s[i : i + len(word)]:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        
        return dfs(0)
            

                
                



        