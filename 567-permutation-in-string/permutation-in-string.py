import string
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1_list, s2_list = [0] * 26, [0] * 26
        matches = 0
        for i in range(len(s1)):
            s1_list[ord(s1[i]) - ord('a')] += 1
            s2_list[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            matches += 1 if s1_list[i] == s2_list[i] else 0

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[right]) - ord('a')
            s2_list[index] += 1
            if s2_list[index] == s1_list[index]:
                matches += 1
            elif s2_list[index] - 1 == s1_list[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2_list[index] -= 1
            if s2_list[index] == s1_list[index]:
                matches += 1
            elif s2_list[index] + 1 == s1_list[index]:
                matches -= 1
            left += 1
        return matches == 26

