class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        return sorted(num_count, key=num_count.get, reverse=True)[:k]