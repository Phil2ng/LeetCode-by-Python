class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        while digits[n] == 9 and n >= 0:
            digits[n] = 0
            n -= 1
        if n >= 0:
            digits[n] += 1
        elif n == -1:
            digits.insert(0,1)
        return digits
