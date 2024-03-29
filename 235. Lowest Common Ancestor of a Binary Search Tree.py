# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q:
            return root
        if root.val > max(p.val, q.val):
            root = self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            root = self.lowestCommonAncestor(root.right, p, q)
        return root
