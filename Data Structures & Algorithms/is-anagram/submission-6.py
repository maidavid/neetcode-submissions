class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = s_map.get(char, 0) + 1

        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = t_map.get(char, 0) + 1

        if s_map == t_map:
            return True
        
        return False
        