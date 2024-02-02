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

        m2 = ""
        for m in range(len(message)):
            m2 = m2 + d.get(message[m])

        return m2