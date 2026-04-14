class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Put all numbers in a set for O(1) lookup.
        # For each number that starts a sequence (num-1 not in set),
        # count how far the sequence extends. Track the longest.
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest

            