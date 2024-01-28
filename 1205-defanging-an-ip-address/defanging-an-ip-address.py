class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        add2 = ""
        for i in address:
            if i == ".":
                add2 = add2 + "[.]"
            else:
                add2 = add2 + i

        return add2