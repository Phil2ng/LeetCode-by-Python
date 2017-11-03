class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        isIn = False
        revenue = 0
        for i in range(len(prices) - 1):
            if isIn is False:
                if prices[i + 1] < prices[i]:
                    continue
                else:
                    isIn = True
                    inPrices = prices[i]
            else:
                if prices[i + 1] > prices[i]:
                    continue
                else:
                    isIn = False
                    revenue += prices[i] - inPrices
        if isIn is True and prices[-1] > inPrices:
            revenue += prices[-1] - inPrices
        return revenue


if __name__ == '__main__':
    s = Solution()
    prices = [4, 5, 3, 2, 10, 1, 6]
    print(s.maxProfit(prices))
