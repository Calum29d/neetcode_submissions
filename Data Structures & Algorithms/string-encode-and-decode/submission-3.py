class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for word in strs:
            res += str(len(word)) + "#" + word #adds a delimiter but also adds the length of the word to make sure we dont stop if there is a # in the word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i #makes j equal to the start position of the next word to decode
            while s[j] != "#": #loops until we find the delimiter char
                j += 1 # everything between i and j will be the length of the word

            length = int(s[i:j]) #gets the length of the word 
            res.append(s[j+1: j+1 + length]) 
            i = j+1 + length #essentially cuts of the word we just processed
        return res

        #this is the efficent solution, I should start thinking more about the possible edge cases as my previous solution didnt account for the delimiter char appearing

