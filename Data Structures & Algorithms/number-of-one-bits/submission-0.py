class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            
            #if bit is 1 remainder will return 1 if 0 then returns 0 to total
            res += n % 2

            #shift bit by 1 to look at next bit
            n = n >> 1
        
        return res
        