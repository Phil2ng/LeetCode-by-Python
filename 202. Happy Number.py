class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = self.next(n)
        while slow != fast:
            slow = self.next(slow)
            fast = self.next(self.next(fast))
        return slow == 1

    def next(self, n):
        ret = 0
        while n:
            ret += (n % 10) * (n % 10)
            n //= 10
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(7))
