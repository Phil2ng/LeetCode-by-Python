class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for c in s:
            res -= ord(c)
        for c in t:
            res += ord(c)
        return chr(res)

        # res = 0
        # for c in s:
        #     res ^= ord(c)
        # for c in t:
        #     res ^= ord(c)
        # return chr(res)
