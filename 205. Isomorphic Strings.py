class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if not self.isTrue(s, t):
            return False
        if not self.isTrue(t, s):
            return False
        return True

    def isTrue(self, s, t):
        sTot = [0] * 256
        for i in range(len(s)):
            tmp = ord(s[i])
            if sTot[tmp] != 0:
                if sTot[tmp] != ord(t[i]):
                    return False
            else:
                sTot[tmp] = ord(t[i])
        return True


if __name__ == '__main__':
    s = Solution()
    res = s.isIsomorphic("adg", "add")
    print(res)
