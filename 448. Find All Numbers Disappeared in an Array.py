class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    s = Solution()
    res = s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print(res)