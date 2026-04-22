class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 pointer approach but i think may solution was easier

        l, r = 0, 1
        maxProfit = 0
        while r != len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r # jump r as r now has the lowest buying price
                r += 1
            else:
                r += 1
        return maxProfit

        #this is O(n) and O(1) aswell, i watched neetCodes explaination and coded it myself though
            

        