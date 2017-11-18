class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for i in range(len(nums)):
            m = a
            n = b
            a = n + nums[i];
            b = max(m, n);
        return max(a, b)
