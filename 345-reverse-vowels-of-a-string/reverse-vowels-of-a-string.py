class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s)-1
        s_arr = list(s)
        while left < right:
            while left < right and s_arr[left] not in vowels:
                left += 1
            while left < right and s_arr[right] not in vowels:
                right -= 1
            temp_left = s_arr[left]
            print(temp_left)
            s_arr[left] = s_arr[right]
            s_arr[right] = temp_left
            left += 1
            right -= 1
        return ''.join(s_arr)

        