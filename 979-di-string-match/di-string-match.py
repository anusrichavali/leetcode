class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        l = [x for x in range(len(s) + 1)]
        nums = []
        for i in s:
            if i == 'I':
                nums.append(l.pop(l.index(min(l))))
            else:
                nums.append(l.pop(l.index(max(l))))
        nums.append(l[0])
        return nums                                                                                     
        