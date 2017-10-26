# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.count(root.left, 1), self.count(root.right, 1))

    def count(self, p, n):
        if p is None:
            return n
        return max(self.count(p.left, n+1), self.count(p.right, n+1))
