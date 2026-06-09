class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)

        if length < 1:
            return ""
        
        ans = strs[0]

        for index, text in enumerate(strs):
            if index == 0:
                continue
            
            i = 0 
            while (i < len(ans) and i < len(text) and ans[i] == text[i]):
                i += 1
            ans = ans[:i]
        
        return ans