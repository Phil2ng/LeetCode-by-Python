class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [True] * (len(nums) + 1)
        for i in nums:
            a[i] = False
        for i in range(len(nums) + 1):
            if a[i]:
                return i


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
