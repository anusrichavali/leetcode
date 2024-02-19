class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        map = {}
        for i in s:
            map[i] = map.get(i, 0) + 1

        for i in t:
            if i not in map.keys():
                return False
            elif map[i] == 0:
                return False
            else:
                map[i] = map.get(i) - 1

        return True