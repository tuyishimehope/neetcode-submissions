class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 0:
            return False
        
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
