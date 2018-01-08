class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        return int((sqrt(8 * n+1)-1)/2)
