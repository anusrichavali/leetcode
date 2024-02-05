class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ct = 0
        l = []
        for i in nums1:
            if i in nums2:
                ct += 1
        l.append(ct)
        ct = 0
        for j in nums2:
            if j in nums1:
                ct += 1
        l.append(ct)
        return l
        