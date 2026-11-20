class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final = 0
        for price_idx in range(0, len(prices)):
            max_profit = 0
            for prev_price in prices[:price_idx]:
                profit = prices[price_idx] - prev_price
                if profit > final:
                    final = profit
        return final
        