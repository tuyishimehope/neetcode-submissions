class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = {}
        for num in nums:
            if num in elements:
                return True
            elements[num] = num
        return False
        