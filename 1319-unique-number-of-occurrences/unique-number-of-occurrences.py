class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        nums = {}
        for i in arr:
            nums[i] = nums.get(i, 0) + 1
        return len(set(nums.values())) == len(nums.values())