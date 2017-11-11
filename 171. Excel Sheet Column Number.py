class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res = res * 26 + ord(s[i]) - ord('A') + 1
        return res
