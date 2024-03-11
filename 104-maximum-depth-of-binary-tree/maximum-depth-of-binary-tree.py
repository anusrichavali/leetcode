# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Logic: use recursion, count the length of the left subtrees
        #count the length of the right subtrees
        #recursively calculate for each so that all the subtrees are counted
        #get the max of the right and left subtrees
        if root is None:
            return 0
        left_sub = 1 + self.maxDepth(root.left)
        right_sub = 1 + self.maxDepth(root.right)
        return max(left_sub, right_sub)
        