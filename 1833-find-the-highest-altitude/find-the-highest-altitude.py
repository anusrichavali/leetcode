class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_alt = 0
        running_alt = 0
        for i in gain:
            running_alt += i
            max_alt = max(max_alt, running_alt)
        return max_alt
        