# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def find(node, k, nodes):
            if node is None:
                return False
            left_val = k - node.val
            if left_val in nodes:
                return True
            nodes.add(node.val)
            return find(node.left, k, nodes) or find(node.right, k, nodes)

        nodes = set([])
        return find(root, k, nodes)
