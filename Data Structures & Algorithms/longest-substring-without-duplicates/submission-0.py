class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        left = 0
        right = 0
        seen = set()

        for index, k in enumerate(s):
            if index == 0:
                longest = max(longest, right - left + 1)
            elif k not in seen :
                longest = max(longest, right - left + 1)
            else:
                while k in seen:
                    seen.remove(s[left])
                    left += 1
            
            seen.add(k)
            right += 1

        return longest