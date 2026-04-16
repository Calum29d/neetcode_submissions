class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = "".join(c for c in s.lower() if c.isalnum()) #didnt know this isalnum function was a thing, only thing that made be struggle a bit
        left = 0
        right = len(string)-1

        while left < right:
            if string[left] != string[right]:
                return False
            else:
                left+=1
                right-=1
        return True
        