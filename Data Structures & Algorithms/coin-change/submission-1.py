class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(amount):
            #reset fewest as we are solving a subproblem for the current amount
            fewest = float("inf")

            #base case
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]
            
            for coin in coins:
                if coin <= amount:
                    fewest = min(fewest, 1 + dfs(amount - coin))
                else:
                    continue

            #save calcluated result
            memo[amount] = fewest
            return fewest
            
        fewest = dfs(amount)
        return fewest if fewest != float("inf") else -1


            

