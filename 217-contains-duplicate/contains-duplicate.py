class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        removeDup = set()
        for i in nums:
            if i in removeDup:
                return True
            removeDup.add(i)
        return False
        