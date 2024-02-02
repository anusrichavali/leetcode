class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        l = ""
        for i in range(len(s)):
            if s[i] == '(':
                count = count + 1
                if count != 1:
                    l = l + '('
            else:
                if count != 1:
                    l = l + ')' 
                count = count - 1 

        return l
        



