class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = [char for char in s]
        t_chars = [char for char in t]

        s_set = {}
        t_set = {}

        for char in s_chars:
            if char in s_set:
                s_set[char] += 1
            else:
                s_set[char] = 1

        for char in t_chars:
            if char in t_set:
                t_set[char] += 1
            else:
                t_set[char] = 1

        return True if s_set == t_set else False  
        