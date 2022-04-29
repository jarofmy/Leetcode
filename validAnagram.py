class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if not s and t:
            return False
        
        if not t and s:
            return False
        
        d = {}
        
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        for char in t:
            if char in d:
                d[char] -= 1
            else:
                return False
            
        for key, value in d.items():
            if value != 0:
                return False
            
        return True