class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sum = 0
        pre = None
        for x in s:
            if pre and numerals[x] > pre:
                sum -= 2 * pre
            sum += numerals[x]
            pre = numerals[x]
        return sum
