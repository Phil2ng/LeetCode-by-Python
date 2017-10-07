class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        len = 1
        while x / len >= 10: len *= 10

        while x > 0:
            if x % 10 != int(x / len):
                return False
            x = int((x - int(x / len) * len) / 10)
            len /= 100
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
