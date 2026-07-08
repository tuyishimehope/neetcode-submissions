class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse= True)

        result = []

        for num, count in sorted_items[:k]:
            result.append(num)
        
        return result
        