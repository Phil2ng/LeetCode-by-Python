# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.help(root.left, root.right)
        return True

    def help(self, p, q):
        if p is None and q is None: return True
        if p and q and p.val == q.val:
            return self.help(p.left, q.right) and self.help(p.right, q.left)
        return False
