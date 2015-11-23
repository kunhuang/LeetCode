class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        total_profit = 0
        sell_price = buy_price = prices[0]
        i = 0

        while i+1 < len(prices):
            while i+1 < len(prices) and prices[i+1] >= prices[i]:
                i += 1

            sell_price = prices[i]
            total_profit += sell_price - buy_price

            while i+1 < len(prices) and prices[i+1] <= prices[i]:
                i += 1
            buy_price = prices[i]
            
        return total_profit

print Solution().maxProfit([1,4,2,5,3,2,3])