class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre = cur = 1
        for i in range(n - 1):
            pre, cur = cur, pre + cur
        return cur


if __name__ == '__main__':
    s = Solution()
    ans = s.climbStairs(6)
    print(ans)
