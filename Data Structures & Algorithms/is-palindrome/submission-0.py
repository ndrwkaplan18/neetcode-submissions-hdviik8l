import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # walk string front -> back
        # and back -> front
        # constructing an array (or new string whatever is faster)
        # skip non alphanumerics
        # compare array/strings
        s = re.sub(r"[^a-z0-9]", "", s.lower())
        return s == s[::-1]
        