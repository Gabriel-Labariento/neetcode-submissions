class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        ht = {}
        
        for c in s:
            if not hs.get(c):
                hs[c] = 1
            else:
                hs[c] = hs[c] + 1
        
        for c in t:
            if not ht.get(c):
                ht[c] = 1
            else:
                ht[c] = ht[c] + 1
        
        if len(ht.keys()) != len(hs.keys()):
            return False
            
        for c in s:
            if not ht.get(c):
                return False

            if hs[c] != ht[c]:
                return False
        return True
