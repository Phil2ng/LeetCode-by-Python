class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.getSum(31, 5))
