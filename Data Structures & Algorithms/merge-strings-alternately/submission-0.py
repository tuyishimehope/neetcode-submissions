class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        word1_len = len(word1)
        word2_len = len(word2)
        n = max(word1_len, word2_len)

        for i in range(n):
            if i < word1_len:
                result += word1[i]
            if i < word2_len:
                result += word2[i]

        return result
