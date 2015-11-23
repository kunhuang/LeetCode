class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        max_profit = 0
        sell_price = buy_price = prices[0]
        i = 0

        while i+1 < len(prices):
            while i+1 < len(prices) and prices[i+1] >= prices[i]:
                i += 1
            if prices[i] > sell_price:
                sell_price = prices[i]
                if sell_price - buy_price > max_profit:
                    max_profit = sell_price - buy_price

            while i+1 < len(prices) and prices[i+1] <= prices[i]:
                i += 1
            if prices[i] < buy_price:
                buy_price = sell_price = prices[i]
            
        if sell_price - buy_price > max_profit:
            max_profit = sell_price - buy_price

        return max_profit

print Solution().maxProfit([1, 4, 5, 6, 0, 7])