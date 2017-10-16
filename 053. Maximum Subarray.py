class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        most = nums[0]  # 到当前元素为止最优的解
        local = nums[0]  # 必须包含当前元素的最优的解
        for n in nums[1:]:
            local = max(n, local + n)
            most = max(local, most)
        return most

        # return divideAndConquer(nums, 0, len(nums) - 1)


def divideAndConquer(nums, left, right):
    if left >= right:
        return nums[left]
    mid = left + int((right - left) / 2)
    lmax = divideAndConquer(nums, left, mid - 1)
    rmax = divideAndConquer(nums, mid + 1, right)

    mmax = nums[mid]
    t = mmax
    for i in range(mid + 1, right + 1):
        t += nums[i]
        mmax = max(mmax, t)
    t = mmax
    for i in range(mid - 1, left - 1, -1):
        t += nums[i];
        mmax = max(mmax, t)
    return max(mmax, max(lmax, rmax))


if __name__ == '__main__':
    s = Solution();
    res = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(res)
