class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        
        min_val = float('inf')
        max_diff = 0
        for current_price in prices:
            if current_price < min_val:
                min_val = current_price
            current_diff = current_price - min_val
            max_diff = max(max_diff, current_diff)
        return max_diff