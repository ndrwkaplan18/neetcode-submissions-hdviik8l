class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + '#' + s
        return output

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            k = int(s[i:j])
            ss = s[j+1:j+1+k]
            result.append(ss)
            i = j + 1 + k
        return result

