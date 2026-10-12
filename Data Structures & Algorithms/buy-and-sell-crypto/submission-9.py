class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        left, right = 0, 1

        while right <= len(prices) - 1:
            current = prices[right] - prices[left]
            if current > profits:
                profits = current
            if current <= 0:
                left = right
            right += 1

        return profits
