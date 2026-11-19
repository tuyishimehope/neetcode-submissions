class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1) - 1
        left, right = 0, size
        s1_dict = {}
        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        while right < len(s2):
            current_dict = {}
            i = left
            while i <= right:
                current_dict[s2[i]] = current_dict.get(s2[i], 0) + 1
                i += 1

            if s1_dict == current_dict:
                return True
            left += 1
            right += 1
        
        return False