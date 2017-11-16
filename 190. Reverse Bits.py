class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1 | (n & 1)
            n >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))
