class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(prices== None or len(prices)==0):
            return 0
        max_p=prices[0]
        profit=0
        for i in range(len(prices)):
            max_p=min(max_p, prices[i])
            profit = max(profit, prices[i]-max_p)
        return profit