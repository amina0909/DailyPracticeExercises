class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        self.exist = False
        def traverse(node, curSum):
            if node is not None:
                curSum += node.val
                if not node.left and not node.right:
                    if curSum == targetSum:
                        self.exist = True
                else:
                    traverse(node.left, curSum)
                    traverse(node.right, curSum)
                curSum -= node.val
        traverse(root, 0)
        return self.exist
