class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        res = 1.0
        pre = 0
        while res != pre:
            pre = res
            res = (res + x / res) / 2
            if int(res) * int(res) == x:
                break
        return int(res)


if __name__ == '__main__':
    s = Solution()
    ans = s.mySqrt(8)
    print(ans)
