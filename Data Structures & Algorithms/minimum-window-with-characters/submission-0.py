class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        shortest = (0, len(s) + 1) # have to make the right pointer huge otherwise we cant compare string length
        l, r = 0, 0

        #count the freqs of each char, needed to ensure we have a valid window
        for char in t:
            need[char] = need.get(char,0) + 1

        required = len(need)
        added = 0

        while r < len(s):

            while added != required and r < len(s):
                if s[r] in need:
                    window[s[r]] = window.get(s[r], 0) + 1
                    if window[s[r]] == need[s[r]]:
                        added += 1
                    r += 1
                else:
                    window[s[r]] = window.get(s[r], 0) + 1
                    r += 1

            while added == required:
                if r - l < shortest[1] - shortest[0]:
                    shortest = (l, r)

                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    added -= 1
                
                l += 1

        if shortest[1] == len(s) + 1:
            return ""
        return s[shortest[0]:shortest[1]]

                
        

            

        