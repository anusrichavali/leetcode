class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ""
        for i in digits:
            string = string + str(i)
        
        value = str(int(string) + 1)
        digits_one = []

        for i in value:
            digits_one.append(int(i))

        return digits_one