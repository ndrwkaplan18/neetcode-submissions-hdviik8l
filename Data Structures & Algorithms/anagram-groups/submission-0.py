class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = self.makeCount(s)  # returns a hashable key
            groups.setdefault(key, []).append(s)
        return list(groups.values())

    def makeCount(self, s: str) -> Tuple[int, ...]:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        return tuple(counts)