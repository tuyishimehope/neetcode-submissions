class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for ch in s:
            if (
                ord("A") <= ord(ch) <= ord("Z")
                or ord("a") <= ord(ch) <= ord("z")
                or ord("0") <= ord(ch) <= ord("9")
            ):
                clean_str += ch.lower()

        left = 0
        right = len(clean_str) - 1

        for i, ch in enumerate(clean_str):
            if clean_str[i] != clean_str[right - i]:
                return False
        return True
