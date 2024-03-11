# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #Logic: use recursion
        #base case: if the root is null, return the root
        #store the left child as temp
        #make the left child the right child
        #equate the right child to temp
        #now call the recursion on the left and right children in order to sort the lower subtrees
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        