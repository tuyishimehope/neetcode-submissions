class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = 0
        count1 = 0

        candidate2 = 0
        count2 = 0

        for i in range(0, len(nums)):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = nums[i]
                count1 = 1
            elif count2 == 0:
                candidate2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        count1 = 0
        count2 = 0
        threshold = len(nums) // 3

        for num in nums:
            if num == candidate1:
                count1 += 1
            if num == candidate2:
                count2 += 1

        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)

        return result
