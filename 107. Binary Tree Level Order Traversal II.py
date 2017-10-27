# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        results = [[root.val]]
        reflist1 = [root]
        while True:
            reflist2 = []
            result = []
            for i in range(len(reflist1)):
                cur = reflist1[i]
                if None != cur.left:
                    reflist2.append(cur.left)
                    result.append(cur.left.val)
                if None != cur.right:
                    reflist2.append(cur.right)
                    result.append(cur.right.val)
            if 0 == len(reflist2):
                break
            results.insert(0, result)
            reflist1 = reflist2
        return results
