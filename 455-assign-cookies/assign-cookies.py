class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        contentKids = 0
        while s and g:
            curr_cookie = s.pop()
            while g:
                greed = g.pop()
                if greed <= curr_cookie:
                    contentKids += 1
                    break
        return contentKids