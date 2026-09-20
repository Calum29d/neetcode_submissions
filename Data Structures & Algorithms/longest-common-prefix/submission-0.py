class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: # if out of bounds or char is not the same
                    return res

            res += strs[0][i]
        
        return res