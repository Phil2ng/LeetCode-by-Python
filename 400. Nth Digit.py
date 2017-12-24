class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit, base, ith = 1, 9, 1
        while n > base * digit:
            n -= base * digit
            digit += 1
            ith += base
            base *= 10
        return ord(str(ith + int((n - 1) / digit))[(n - 1) % digit]) - ord('0')
