class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common = (set(nums1)).intersection(set(nums2))
        ct1 = ct2 = 0
        for i in common:
            ct1 += nums1.count(i)
            ct2 += nums2.count(i)
        return [ct1, ct2]
        
        
        