# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]

        def depthFirstSearch(root):
            if root == None:
                return -1
            leftLength = depthFirstSearch(root.left)
            rightLength = depthFirstSearch(root.right)
            result[0] = max(result[0], leftLength + rightLength + 2)

            return 1 + max(leftLength, rightLength)

        depthFirstSearch(root)
        return result[0]
        

        