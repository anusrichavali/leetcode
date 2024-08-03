# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leaves(self, root, leaves):
        if not root:
            return
        if root.left is None and root.right is None:
            leaves.append(root.val)
        self.leaves(root.left, leaves)
        self.leaves(root.right, leaves)
        return leaves

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = []
        leaf2 = []
        print(self.leaves(root1, leaf1))
        print(self.leaves(root2, leaf2))
        return leaf1 == leaf2


        