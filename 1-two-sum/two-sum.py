class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i in range(0, len(nums)):
            if nums[i] in diffs.keys():
                return [diffs.get(nums[i]), i]
            diffs[target - nums[i]] = i
        