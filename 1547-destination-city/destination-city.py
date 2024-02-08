class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        s = [i[0] for i in paths]
        e = [i[1] for i in paths]
        dest = ""
        for j in e:
            if j not in s:
                dest = j
                return dest
        
