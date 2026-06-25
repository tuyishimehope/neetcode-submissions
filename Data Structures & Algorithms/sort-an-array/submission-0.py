class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for current in range(n):
            min_index = current
            for i in range(current + 1, n):
                if nums[i] < nums[min_index]:
                    min_index = i       
            nums[current], nums[min_index] = nums[min_index], nums[current]
        
        return nums