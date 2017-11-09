class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        str = ""
        while n != 0:
            n -= 1
            str += chr(ord('A') + int(n % 26))
            n = int(n / 26)
        str = str[::-1]
        return str


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(26))
