class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char for char in s.lower() if char.isalnum())

        l = 0
        r = len(clean_text) - 1
        i = 0
        while i < len(clean_text) - 1:
            if clean_text[l] != clean_text[r]:
                return False
            l += 1
            r -= 1
            i += 1
        return True
            