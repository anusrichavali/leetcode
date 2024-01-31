class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        nums.sort()
        for i in range(1, len(nums), 2):
            arr.append(nums[i])
            arr.append(nums[i - 1])        
        return arr