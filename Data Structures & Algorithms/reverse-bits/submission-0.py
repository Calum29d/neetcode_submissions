class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):
            #make room for the next bit to be inserted
            res = res << 1

            #get the LSB from n
            bit = n & 1

            #put the bit onto the res
            res += bit
            #finally shift n so we can read the next bit
            n = n >> 1
        
        return res

        
        