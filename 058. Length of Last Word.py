class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 先将字符串后面的空格部分删除，再按照空格字符将剩余部分分成若干部分，
        # 此时最后一部分即为最后一个单词（也可能是”），直接返回其长度即可
        return len(s.rstrip().split(' ')[-1])
