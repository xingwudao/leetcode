# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)
        root.left, root.right = inverted_right, inverted_left
        
        return root
