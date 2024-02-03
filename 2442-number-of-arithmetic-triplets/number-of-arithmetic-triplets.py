class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        ct = 0
        for i in nums:
            if (i + diff) in nums and (i + diff + diff) in nums:
                ct += 1
        
        return ct
            

                