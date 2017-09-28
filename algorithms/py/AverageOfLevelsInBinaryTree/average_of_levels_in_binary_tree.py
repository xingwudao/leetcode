class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        levelInfo = []
        def getDepthAndSum(node, depth):
            if node is None:
                return
            if len(levelInfo) <= depth:
                levelInfo.append([0, 0])
            levelInfo[depth][0] += node.val
            levelInfo[depth][1] += 1
            getDepthAndSum(node.left, depth + 1)
            getDepthAndSum(node.right, depth + 1 )

        getDepthAndSum(root, 0)
        return list(map(lambda x: x[0]/x[1], levelInfo))
