class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        difLp = [0] * len(prices)
        minp = prices[0]
        for i in range(1, len(prices)):
            minp = prices[i] if prices[i] < minp else minp
            difLp[i] = prices[i] - minp
        return max(difLp)
