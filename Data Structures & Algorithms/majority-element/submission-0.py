import math 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen_map = {}

        for num in nums:
            if num in seen_map:
                seen_map[num] += 1
            else:
                seen_map[num] = 1
        
        size = round(len(nums) / 2)

        for el, count in seen_map.items():
            if count >= size:
                return el

        