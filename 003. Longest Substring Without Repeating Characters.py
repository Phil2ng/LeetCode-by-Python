class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {}
        i, ans = 0, 0
        for j in range(len(s)):
            i = max(i, index.get(s[j], 0))
            ans = max(ans, j - i + 1)
            index[s[j]] = j + 1
        return ans

        # index = [0] * 128
        # i, ans = 0, 0
        # for j in range(len(s)):
        #     i = max(i, index[s[j]])
        #     ans = max(ans, j - i + 1)
        #     index[s[j]] = j + 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)
