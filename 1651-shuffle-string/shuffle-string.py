class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffle = [0] * len(s)
        for i in range(len(s)):
            shuffle[indices[i]] = s[i]
        return ''.join(shuffle)