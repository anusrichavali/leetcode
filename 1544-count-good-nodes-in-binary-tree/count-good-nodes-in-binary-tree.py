# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(self, root, greatest):
            if not root:
                return 0
            if root.val >= greatest:
                count = 1
            else:
                count = 0
            greatest = max(root.val, greatest)
            count += dfs(self, root.left, greatest)
            count += dfs(self, root.right, greatest)
            return count
        return dfs(self, root, root.val)
        