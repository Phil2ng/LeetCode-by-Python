class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = 1 if x >= 0 else -1
        x *= t;

        # result = 0
        # while x:
        #     result = result * 10 + x % 10
        #     x /= 10
        #
        # if result>2147483647 or result<-2147483648:
        #     return 0
        # else:
        #     return result*t

        x = t * int(str(x)[::-1])
        return x if -2147483648 <= x <= 2147483647 else 0
