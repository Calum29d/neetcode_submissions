class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += word + "£" 
        
        return res
        


    def decode(self, s: str) -> List[str]:
        res = []

        if len(s) == 0:
            return []
        elif s[-1] == "£":
            s = s[:-1] #remove the last hashtag as it gets added at the end of every word so it doesnt split an empty string

        res = s.strip().split("£")
        return res

        #definetly a slow solution, never done one like this before.
        #ok i cant use a hashtag as its part of the ascii char set, should have realised that.
        #what if i just use a character thats not in the ascii set?
        
            

