class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = s.split(' ')
        print(len(ls))
        l = ['0'] * len(ls)
        for i in ls:
            index = int(i[len(i) - 1])
            l[index - 1] = i[0:len(i) - 1]
        
        return ' '.join(l)
        