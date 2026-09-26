class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # no point in eating more than the max pile   
        res = r

        while l <= r:
            k = l + (r - l) // 2 # amount of bananas we are choosing to eat / middle
            curTime = 0

            for p in piles:
                if p < k:
                    curTime += 1
                else:
                    curTime += math.ceil(p/k)
            
            if curTime <= h: # if valid time
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1

        return res

        # O(nlogn) time O(1) space
        






       