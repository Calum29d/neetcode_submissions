class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles) # the range of how many bananas koko can choose to eat
        res = end

        while start <= end:
            k = (start + end) // 2 #how many bananas koko is eating
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k) #get how long it take to eat this pile
            
            if hours <= h: #if its a time taken is within limit
                res = min(res, k)
                end = k - 1
            else: #otherwise koko would take to long to eat all piles so we have to choose to eat more bananas 
                start = k + 1
            
        return res

        #O(n * log(max(piles))) and O(1) space
