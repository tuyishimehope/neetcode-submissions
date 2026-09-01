class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        left = 0
        right = 0

        for c in range(len(t) - 1):
            # if t[left] == t[left + 1]:
                # continue
            print(right)
            if right > len(s) - 1:
                return True
            if t[left] == s[right]:
                left += 1
                right += 1
            else:
                left += 1

        if right < len(s) - 1:
            return False
        print(right)
        print(len(s) -1)
        return True