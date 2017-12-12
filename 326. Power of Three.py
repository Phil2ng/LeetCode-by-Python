class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:

            if n == 1:
                return True
            if n % 3 != 0:
                return False
            n = int(n / 3)
