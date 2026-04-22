class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i]) #you always want to buy at the lowest price
            maxProfit = max(maxProfit, prices[i] - minPrice) #calculates the profit for the current minPrice and from the current position in the array
        return maxProfit








        