class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        removeDup = set(nums)
        if len(removeDup) < len(nums):
            return True
        return False
        