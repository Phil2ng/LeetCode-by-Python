class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = res = 0
        for i in nums:
            if i == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
        return max(res, cnt)
