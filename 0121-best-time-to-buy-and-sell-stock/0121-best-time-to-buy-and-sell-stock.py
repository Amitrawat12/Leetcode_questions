class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for i in range(len(prices)):
            if (profit < (prices[i]-min)):
                profit = prices[i]-min
            if min > prices[i]:
                min = prices[i]
        return profit