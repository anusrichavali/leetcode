class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l_new = []
        for i in nums:
            for j in str(i):
                l_new.append(int(j))
        return l_new
        