class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index = 0
        actual = 0
        for i, num in enumerate(nums):
            index += i + 1
            actual += num
        return index - actual