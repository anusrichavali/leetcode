class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e = 0
        a = 0
        for i in nums:
            e += i
            for j in str(i):
                a += int(j)
        
        return abs(e - a)
        