class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []

        
        def countOnes(num):
            count = 0

            while num:
                count += num % 2
                num = num >> 1

            return count
        
        #count ones for each number in range of n and append to array
        for i in range(n + 1):
            res.append(countOnes(i))
        
        return res

        #should be O(n) as countOnes is a O(32) time operation so O(1) and we go through every num up to n
        #space O(n)