class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        for i in range(k):
            m = max(nums)
            s += nums.pop(nums.index(max(nums)))
            nums.append(m + 1)
        return s
        