class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 1.库函数string.find()
        # return haystack.find(needle)

        # 2.扫描haystack
        # if not needle:
        #     return 0
        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i] == needle[0]:
        #         j = 1
        #         while j < len(needle) and haystack[i + j] == needle[j]:
        #             j += 1
        #         if j == len(needle):
        #             return i
        # return -1

        # 3.类似substring的方法简化上面的代码
        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i:i + len(needle)] == needle:
        #         return i
        # return -1

        # 4.KMP算法 O(n+m)
        if not needle:
            return 0
        # generate next array, need O(n) time
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:
            # needle[k] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
        # check through the haystack using next, need O(m) time
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1