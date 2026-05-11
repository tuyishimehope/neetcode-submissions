class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 0:
            return False

        elements = set()
        
        for num in nums:
            if num in elements:
                return True
            elements.add(num)
        return False
        