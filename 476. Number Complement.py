class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return ~(-1 << num.bit_length()) & ~num
