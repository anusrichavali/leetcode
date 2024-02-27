class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            middle = (left + right)/2
            if target <= middle:
                if nums[left] <= middle:
                    right -= 1
                else:
                    left += 1
            else:
                if nums[left] <= middle:
                    left += 1
                else:
                    right -= 1
        return -1