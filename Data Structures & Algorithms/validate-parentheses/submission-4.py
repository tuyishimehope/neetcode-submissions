class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        start_bracket = {"[", "{", "("}
        end_bracket = {"]", "}", ")"}

        store = []

        for char in s:
            if char in start_bracket:
                store.append(char)

            if char in end_bracket:
                if len(store) >= 1:
                    last = store.pop()
                else:
                    return False

                cor = ""
                if last == "[":
                    cor = "]"
                elif last == "{":
                    cor = "}"
                elif last == "(":
                    cor = ")"

                if char == cor:
                    continue
                return False

        if len(store) >= 1:
            return False
        return True
