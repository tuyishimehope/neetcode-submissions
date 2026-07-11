class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1 or len(s) > 1000:
            return False
        
        valid_str = "".join(char for char in s.lower() if char.isalnum())
        length = len(valid_str)
        
        updated_str = ""
        for char in range(length -1, -1, -1):
            if valid_str[char].isalnum() and (valid_str[char].islower() or valid_str[char].isdigit()):
                updated_str += valid_str[char]

        if valid_str == updated_str:
            return True
        else :
            return False
        