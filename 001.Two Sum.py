class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            t = target - nums[i]
            if t in nums[i + 1:]:
                return i, nums[i + 1:].index(t) + i + 1

        # dic = dict()
        # for index, value in enumerate(nums):
        #     sub = target - value
        #     if sub in dic:
        #         return [dic[sub], index]
        #     else:
        #         dic[value] = index
