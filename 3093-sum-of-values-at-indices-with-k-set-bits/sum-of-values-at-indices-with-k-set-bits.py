class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        for i in range(len(nums)):
            count = 0
            for j in str(bin(i)):
                if j == '1':
                    count = count + 1
            if count == k:
                sum = sum + nums[i]
        return sum

        return sum
        