# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        res = self.sumOfLeftLeaves(root.right)
        if root.left is not None and root.left.left is None and root.left.right is None:
            res += root.left.val
        res += self.sumOfLeftLeaves(root.left)
        return res
