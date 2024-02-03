class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(0, len(arr) + 1 - i, 1):
                l = arr[j: j + i: 1]
                print(l)
                s += sum(l)
        return s
        