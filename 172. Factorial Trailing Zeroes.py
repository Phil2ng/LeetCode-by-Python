class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += int(n / 5)
            n = int(n / 5)
        return count
