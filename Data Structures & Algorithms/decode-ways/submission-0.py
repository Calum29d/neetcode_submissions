class Solution:
    def numDecodings(self, s: str) -> int:
        #bottom up DP solution O(n) time and space

        #create dp table and fill first slot with corresponding number so we can reuse it for next steps
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1

        if s[0] == "0":
            return 0
        else:
            dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i-1] == "0":
                #if we find a zero make sure that it can be put together as 10 or 20 other wise not decodable
                if s[i-2] == "1" or s[i-2] == "2":
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                #make sure between 10 and 26
                if(s[i-2] == "1") or (s[i-2] == "2" and int(s[i-1]) < 7):
                    dp[i] = dp[i-2] + dp[i-1]
                
                else:
                    dp[i] = dp[i-1]
                

        return dp[len(s)]

        