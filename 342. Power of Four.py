class Solution:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:
            if n == 1:
                return True
            if n % 4 != 0:
                return False
            n = int(n / 4)
