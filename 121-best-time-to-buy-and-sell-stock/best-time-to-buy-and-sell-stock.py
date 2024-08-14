class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            sell = prices[i]
            if sell > buy:
                max_profit = max(max_profit, sell - buy)
            else:
                buy = sell
        return max_profit