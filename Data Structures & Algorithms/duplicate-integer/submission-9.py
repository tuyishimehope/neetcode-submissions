class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 0:
            return False
        
        seen_num = {}

        for num in nums:
            if num in seen_num:
                return True
            seen_num[num] = num
        
        return False
