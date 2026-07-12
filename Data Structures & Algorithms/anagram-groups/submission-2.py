class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            character_counts = [0] * 26
            for ch in word:
                character_counts[ord(ch) - ord("a")] += 1
            signature = tuple(character_counts)

            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature] = [word]

        return list(groups.values())
