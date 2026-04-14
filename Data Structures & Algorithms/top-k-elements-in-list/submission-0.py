class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            count = num_count.setdefault(num, 0)
            num_count[num] = count + 1
        
        return sorted(num_count, key=num_count.get, reverse=True)[:k]