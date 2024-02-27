class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                min_val = min(min_val, nums[left])
                break 

            middle = (left + right)//2
            min_val = min(min_val, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return min_val
        