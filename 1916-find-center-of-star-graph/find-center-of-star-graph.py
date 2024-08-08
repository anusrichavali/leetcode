class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        used = set()
        for u, v in edges:
            if u in used:
                return u
            if v in used:
                return v
            used.add(u)
            used.add(v)