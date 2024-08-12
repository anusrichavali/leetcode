class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left = right = 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
            print(k)
        return right - left - 1