class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        seen = {}
        result = []

        end = 0
        for i, ch in enumerate(s):
            seen[ch] = i

        for i, ch in enumerate(s):
            size += 1
            end = max(end, seen[ch])
            if i == end:
                result.append(size)
                size = 0

        return result
