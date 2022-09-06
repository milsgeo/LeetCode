class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(prices== None or len(prices)==0):
            return 0
        # max_p=prices[0]
        # profit=0
        # for i in range(len(prices)):
        #     max_p=min(max_p, prices[i])
        #     profit = max(profit, prices[i]-max_p)
        # return profit
        
        min_price=float('inf')
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            elif prices[i]-min_price > max_profit:
                max_profit=prices[i]-min_price
        return max_profit