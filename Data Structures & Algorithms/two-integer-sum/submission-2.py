class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2 or len(nums) > 1000:
            return
        
        prev_map = {}

        for i, el in enumerate(nums):
            diff = target - el

            if diff in prev_map:
                return [prev_map[diff], i]

            prev_map[el] = i
        
        