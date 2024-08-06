class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_vowels = 0
        curr_vowels = 0
        vowels = set('aeiou')
        for i in range(k):
            if s[i] in vowels:
                curr_vowels += 1
        max_vowels = curr_vowels

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                curr_vowels -= 1
            if s[i] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels