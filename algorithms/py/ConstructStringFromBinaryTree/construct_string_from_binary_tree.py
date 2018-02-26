class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        
        left_str = self.tree2str(t.left)
        right_str = self.tree2str(t.right)
        
        if len(right_str) > 0:
            return "%s(%s)(%s)" % (str(t.val), left_str, right_str)
        elif len(left_str) == 0:
            return str(t.val)
        else:
            return "%s(%s)" % (str(t.val), left_str)
