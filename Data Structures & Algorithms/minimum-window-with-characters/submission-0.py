class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        tSet, window = {}, {}
        for c in t:
            tSet[c] = 1 + tSet.get(c, 0)
        
        window = {}
        for k in tSet.keys():
            window[k] = 0

        l = 0
        have, need = 0, len(tSet)
        res, resLen = [-1, -1], float('infinity')
        for r in range(len(s)):
            c = s[r]
            if c in tSet:
                if c in window: window[c] += 1
                else: window[c] = 1

                if c in tSet and window[c] == tSet[c]: 
                    have += 1

                while have == need:
                    if r - l + 1 < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                    
                    if s[l] in window:
                        window[s[l]] -= 1
                        if s[l] in tSet and window[s[l]] < tSet[s[l]]: have -=1
                    l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
            
                

        

        