class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        
        for index, item in enumerate(nums):
            if index > 0 and item == nums[index - 1]:
                continue

            target = 0 - item
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if (nums[left] + nums[right])  > target:
                    right -= 1
                elif (nums[left] + nums[right]) < target:
                    left += 1
                else:
                    result.append([item, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
        