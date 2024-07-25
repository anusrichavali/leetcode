class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        s_ptr = 0
        t_ptr = 0
        while s_ptr < len(s) and t_ptr < len(t):
            while t_ptr < len(t) and t[t_ptr] != s[s_ptr]:
                t_ptr += 1
            if t_ptr < len(t) and t[t_ptr] == s[s_ptr]:
                s_ptr += 1
                t_ptr += 1
        return s_ptr == len(s)
        