class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s = 0
        ct = 0
        for i in mat:
            if ct != len(i) - 1 - ct:
                s += i[ct] + i[len(i) - 1 - ct]
            else:
                s+= i[ct]
            ct += 1
        
        return s