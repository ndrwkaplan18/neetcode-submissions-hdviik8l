class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}    
        for s_char in s:
            if s_char in s_map:
                s_map[s_char] += 1
            else:
                s_map[s_char] = 1
        
        for t_char in t:
            if t_char in t_map:
                t_map[t_char] += 1
            else:
                t_map[t_char] = 1
        
        for char in s:
            if s_map.get(char) != t_map.get(char):
                return False
        return True

