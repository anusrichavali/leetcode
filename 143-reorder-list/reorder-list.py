# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        first, second = head, head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        
        slow = first.next
        prev = first.next = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        fast, slow = head, prev
        while slow:
            tmp1, tmp2 = fast.next, slow.next
            fast.next = slow
            slow.next = tmp1
            fast, slow = tmp1, tmp2
            


        