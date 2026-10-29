class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left, right = 0, 0

        while right <= len(s) - 1:
            if s[right] not in seen:
                seen.add(s[right])
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
            right += 1
            longest = max(longest, len(seen))

        return longest
