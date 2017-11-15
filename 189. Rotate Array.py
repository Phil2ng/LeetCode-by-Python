class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k, start, n = k % len(nums), 0, len(nums)
        while k % n != 0 and n > 0:
            for i in range(k):
                nums[start + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[start + i]
            start, n = start + k, n - k
            k = k % n
