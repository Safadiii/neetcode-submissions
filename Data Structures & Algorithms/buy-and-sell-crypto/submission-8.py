class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_so_far = 10929029033232
        profit = 0
        for price in prices:
            if price < lowest_so_far:
                lowest_so_far = price
            if price - lowest_so_far > profit:
                profit = price - lowest_so_far
        return profit  