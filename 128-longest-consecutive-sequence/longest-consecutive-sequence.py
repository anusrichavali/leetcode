class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        longest = 0
        for i in nums:
            temp = i
            seq = 0
            if i - 1 not in hashset:
                seq += 1
                while temp + 1 in hashset:
                    seq += 1
                    temp += 1
                if seq > longest:
                    longest = seq
            else:
                continue
        return longest

        