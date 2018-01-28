# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.previous = self.minimum = float('inf')

        def inorder(node):
            if node:
                inorder(node.left)
                self.minimum = min(self.minimum, abs(node.val - self.previous))
                self.previous = node.val
                inorder(node.right)

        inorder(root)
        return self.minimum
