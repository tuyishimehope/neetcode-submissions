class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for el in strs:
            encoded_str = ""
            length = len(el)
            encoded_str = f"{length}#{el}"
            encode += encoded_str
        return encode
        
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_str = []

        while i < len(s):
            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1

            i += 1
            length = int(length)
                    
            recovered = ""

            for _ in range(length):
                recovered += s[i]
                i += 1

            decoded_str.append(recovered)

        return decoded_str