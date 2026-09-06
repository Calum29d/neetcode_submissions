class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        if len(arr) < k:
            return 0
        
        res = 0
        windowSum = 0
        
        l = 0
        for r in range(len(arr)):
            windowSum += arr[r]

            if (r - l) + 1 > k:
                windowSum -= arr[l]
                l += 1
            if (r - l) + 1 == k and windowSum / k >= threshold:
                res += 1
             
        return res




        