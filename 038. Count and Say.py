class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(1, n):
            s1 = ""
            cnt = 1
            for j in range(1, len(s)):
                if s[j] != s[j - 1]:
                    s1 = s1 + str(cnt) + s[j - 1]
                    cnt = 1
                else:
                    cnt = cnt + 1
            s1 = s1 + str(cnt) + s[len(s)-1]
            s = s1
        return s


if __name__ == '__main__':
    s = Solution()
    res = s.countAndSay(5)
    print(res)
