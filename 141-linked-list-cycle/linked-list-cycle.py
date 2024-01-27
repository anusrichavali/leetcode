# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        h = head
        n = head.next
        
        while h != n:
            if not n or not n.next:
                return False
            h = h.next
            n = n.next.next
        return True
        