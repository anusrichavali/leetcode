class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = 0
        pos = len(nums) - 1
        res = []
        while neg <= pos:
            if pow(nums[neg], 2) >= pow(nums[pos], 2):
                res.insert(0, pow(nums[neg], 2))
                neg += 1
            elif pow(nums[pos], 2) > pow(nums[neg], 2):
                res.insert(0, pow(nums[pos], 2))
                pos -= 1
        return res