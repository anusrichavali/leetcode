class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first = s[0:len(s)/2: 1]
        second = s[len(s)/2: len(s)]
        ct1 = ct2 = 0
        for i in range(len(s)/2):
            if first[i] in vowels:
                ct1 += 1
            
            if second[i] in vowels:
                ct2 += 1
        return ct1 == ct2
        