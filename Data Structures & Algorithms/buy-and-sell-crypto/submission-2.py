class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0 
        for r in range(1,len(prices)):
            #calculate current profit
            if prices[l] < prices[r]:
                cur_profit = prices[r] - prices[l]
                max_profit = max(cur_profit,max_profit)
            else:
                #no better options in between so we skip to r 
                l = r
        return max_profit

        