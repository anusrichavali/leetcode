class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        d = {' ': ' '}
        ctr = 0
        for i in key:
            if i not in d.keys():
                d[i] = string.ascii_lowercase[ctr]
                ctr = ctr + 1

        for m in range(len(message)):
            message = message[0:m] + d.get(message[m]) + message[m + 1: len(message)]

        return message