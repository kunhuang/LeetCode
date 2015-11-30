class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        diff = [0]*len(prices)
        for i in range(1, len(prices)):
            diff[i] = prices[i] - prices[i-1]

        left_max_sum = [0]*len(prices)
        right_max_sum = [0]*len(prices)
        max_sum = 0
        current_sum =0

        for i in range(len(diff)):
            if diff[i] >= 0:
                current_sum += diff[i]
                if current_sum > max_sum:
                    max_sum = current_sum
            else:
                current_sum += diff[i]  
                if current_sum < 0:
                    current_sum = 0
            left_max_sum[i] = max_sum

        max_sum = 0
        current_sum =0
        for i in range(len(diff)-2, -1, -1):
            if diff[i+1] >= 0:
                current_sum += diff[i+1]
                if current_sum > max_sum:
                    max_sum = current_sum
            else:
                current_sum += diff[i+1]
                if current_sum < 0:
                    current_sum = 0
            right_max_sum[i] = max_sum

        max_profit = max(map(sum, zip(left_max_sum, right_max_sum)))

        return max_profit
print Solution().maxProfit([1, 3, 4, 5])