# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def breadthFirstSearch(root):
            queue = collections.deque()
            queue.append(root)
            while queue:
                qLen = len(queue)
                level = []
                for i in range(qLen):
                    node = queue.popleft()
                    if node:
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if level:
                    result.append(level[-1])
        
        breadthFirstSearch(root)
        return result
        