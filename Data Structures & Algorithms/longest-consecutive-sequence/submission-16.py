class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in seen:
            current = 1
            if n - 1 not in seen:
                while n + 1 in seen:
                    current += 1
                    n += 1
            longest = max(longest, current)

        return longest
