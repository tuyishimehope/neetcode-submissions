class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        
        for string in strs:
            len_str = len(string)
            encoded_str +=  f"{len_str}#{string}"
        print(encoded_str)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):

            # Find separator '#'
            j = i

            while s[j] != '#':
                j += 1

            # Extract length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract actual string
            word = s[j:j + length]

            result.append(word)

            # Move pointer to next encoded segment
            i = j + length

        return result
