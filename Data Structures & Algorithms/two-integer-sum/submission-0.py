class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in num_set:
                return [num_set.get(difference), index]
            else:
                num_set[num] = index
