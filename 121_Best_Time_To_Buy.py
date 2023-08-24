class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_Profit = int(0)
        min_Profit = prices[0]
        for i in range(0, n):
            if(prices[i] < min_Profit):
                min_Profit = prices[i]
            max_Profit = max(max_Profit, abs(prices[i] - min_Profit))
        else:
            return max_Profit
