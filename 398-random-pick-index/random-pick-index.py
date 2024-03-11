class Solution(object):
    import random

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.map = {i: [] for i in nums}
        for i in range(len(nums)):
            curr = self.map.get(nums[i])
            curr.append(i)
            new_val = {nums[i]: curr}
            self.map.update(new_val)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        curr = self.map.get(target)
        return random.choice(curr)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)