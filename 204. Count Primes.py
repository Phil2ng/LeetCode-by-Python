class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        a = [True] * n
        for i in range(n):
            a[i] = True
        for i in range(2, n):
            if a[i]:
                for j in range(i * i, n, i):
                    a[j] = False
        for i in range(2, n):
            if a[i]:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(49979))
