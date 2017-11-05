class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result

        # nums.sort()
        # for i in range(1, len(nums), 2):
        #     if nums[i] != nums[i - 1]:
        #         return nums[i - 1]
        # return nums[-1]
