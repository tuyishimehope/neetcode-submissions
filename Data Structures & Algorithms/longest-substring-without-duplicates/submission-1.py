class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, left, right = 0, 0, 0
        seen = set()

        for index, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1

            longest = max(longest, right - left + 1)
            seen.add(ch)
            right += 1

        return longest
