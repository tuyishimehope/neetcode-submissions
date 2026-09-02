class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        result = []
        for n in nums1_set:
            for k in nums2_set:
                if n == k:
                    result.append(n)
        return result
            