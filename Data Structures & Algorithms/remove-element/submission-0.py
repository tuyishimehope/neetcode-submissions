class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for index, num in enumerate(nums):
            if num == val:
                pass
            else:
                nums[write] = nums[index]
                write += 1

        return write
