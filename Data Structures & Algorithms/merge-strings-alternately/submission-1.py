class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = [] # list is more efficent than creating a new string for every append
        l, r = 0, 0
        
        while l < len(word1) and r < len(word2):
            res.append(word1[l])
            res.append(word2[r])
            l += 1
            r += 1
        
        res.append(word1[l:])
        res.append(word2[r:])
        
        return "".join(res)

        # Time: O(len(word1) + len(word2))
        # Space: O(len(word1) + len(word2))


        
        