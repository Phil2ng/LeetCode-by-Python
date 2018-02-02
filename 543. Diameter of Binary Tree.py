# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.ans

    def depth(self, p):
        if not p: return 0
        left, right = self.depth(p.left), self.depth(p.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1
