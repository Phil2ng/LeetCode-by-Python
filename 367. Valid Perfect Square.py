class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = int((x + num / x) / 2)
        return x * x == num

        # i = 1
        # while num > 0:
        #     num -= i
        #     i += 2
        # return num == 0
