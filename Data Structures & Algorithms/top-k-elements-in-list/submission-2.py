class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.setdefault(num, 0) + 1
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        count_list = list(sorted_count)
        return count_list[0:k]