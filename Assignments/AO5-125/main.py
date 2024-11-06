class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(letter for letter in s if letter.isalnum())
        s = s.lower()
        s_reverse = s[::-1]
        if s == s_reverse:
            return True
        else:
            return False
