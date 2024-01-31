class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        totals = []
        for i in accounts:
            total = 0
            for j in i:
                total = total + j
            totals.append(total)
        return max(totals)