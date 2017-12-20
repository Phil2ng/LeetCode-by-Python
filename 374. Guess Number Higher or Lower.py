# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid1 = low + (high - low) / 3
            mid2 = high - (high - low) / 3
            res1 = guess(mid1)
            res2 = guess(mid2)
            if res1 == 0:
                return mid1
            if res2 == 0:
                return mid2
            if res1 < 0:
                high = mid1 - 1
            elif res2 > 0:
                low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1
        return -1
