class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #will store the lsc from a tuple of indices (i, j)
        memo = {}

        #i, index text1, j index of text2
        def dfs(i, j):
            
            #if lsc from this postion has already been calculated
            if (i, j) in memo:
                return memo[(i, j)]

            #out of bounds base case
            if i == len(text1) or j == len(text2):
                return 0

            #if chars are equal add 1 to lsc and start dfs on next char
            if text1[i] == text2[j]:
                memo[(i, j)] =  1 + dfs(i+1, j+1)

                #if chars dont match
            else:
                memo[(i, j)] =  max(dfs(i+1, j), dfs(i, j + 1))

            return memo[(i, j)]
        
        return dfs(0,0)

    #O(n * m) time and space where n is len of text1 and m is len of text2
        
