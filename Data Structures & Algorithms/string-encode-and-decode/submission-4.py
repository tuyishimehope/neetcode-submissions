class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for string in strs:
            len_str = len(string)
            encoded +=  f"{len_str}#{string}"

        return encoded


    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1 
    
            length = int(s[i:j])
        
            j += 1
            word = s[j:j + length]
        
            result.append(word)
        
            i = j + length

        return result
