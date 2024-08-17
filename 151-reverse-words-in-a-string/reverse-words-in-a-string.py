class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = ""
        curr = ""
        i = 0
        while i < len(s):
            if s[i] == " " and curr == "":
                i += 1
                continue
            if s[i] == " ":
                if not new_str:
                    new_str = curr
                else:
                    new_str = curr + " " + new_str
                curr = ""
                i += 1
            else:
                curr += s[i]
                i += 1
        if curr:
            if not new_str:
                new_str = curr
            else:
                new_str = curr + " " + new_str
        return new_str
