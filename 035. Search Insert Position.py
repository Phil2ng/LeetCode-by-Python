class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        t = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                t = 1
                break
        return i if t == 1 else len(nums)


if __name__ == '__main__':
    s = Solution()
    res = s.searchInsert([1, 3, 5, 6], 7)
    print(res)
