class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if gas is None or cost is None or len(gas) == 0 or len(cost) == 0:
            return -1
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        N = len(gas)
        diff = map(lambda (x, y): x - y, zip(gas, cost))
        start = 0
        end = 1
        diff_sum = diff[0]
        while start != end:
            if diff_sum >= 0:
                diff_sum += diff[end]
                end = (end + 1)%N
            else:
                start = (start - 1)%N
                diff_sum += diff[start]
        if diff_sum >= 0:
            return start
        else:
            return -1

gas = [-2, 1, 1]
cost = [0, 0, 0]

print Solution().canCompleteCircuit(gas, cost)