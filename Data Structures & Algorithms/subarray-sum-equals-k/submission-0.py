class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        current_prefix = 0
        answer = 0

        for num in nums:
            current_prefix += num

            if current_prefix - k in prefix:
                answer += prefix[current_prefix - k]

            prefix[current_prefix] = prefix.get(current_prefix, 0) + 1

        return answer
