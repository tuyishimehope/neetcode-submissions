class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)

        if length < 1:
            return []

        ans = []
        count = 1
        while(count <= 2):
            for index, num in enumerate(nums):
                ans.append(num)
            count+=1

        return ans
