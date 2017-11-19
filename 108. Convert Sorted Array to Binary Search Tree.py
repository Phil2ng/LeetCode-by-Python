# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None:
            return None
        return self.toBBT(nums, 0, len(nums) - 1)

    def toBBT(self, nums, l, r):
        if l > r:
            return None
        m = int((l + r) / 2)
        root = TreeNode(nums[m])
        root.left = self.toBBT(nums, l, m - 1)
        root.right = self.toBBT(nums, m + 1, r)
        return root
