class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        abbr_ptr, word_ptr = 0, 0
        while abbr_ptr < len(abbr) and word_ptr < len(word):
            num = ''
            if abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr] == '0':
                    return False
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    num += abbr[abbr_ptr]
                    abbr_ptr += 1
                num = int(num)
                word_ptr += num
            else:
                if abbr[abbr_ptr] != word[word_ptr]:
                    return False
                abbr_ptr += 1
                word_ptr += 1
        return abbr_ptr == len(abbr) and word_ptr == len(word)