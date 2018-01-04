class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry, res = 0, ''
        len1, len2 = len(num1), len(num2)
        for i in range(max(len1, len2)):
            n1, n2 = 0, 0
            if i < len1:
                n1 = int(num1[len1 - i - 1])
            if i < len2:
                n2 = int(num2[len2 - i - 1])
            tmp = n1 + n2 + carry
            res = str(tmp % 10) + res
            carry = tmp // 10
        if carry:
            res = str(carry) + res
        return res
