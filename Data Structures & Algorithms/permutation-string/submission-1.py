class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_to_freq = self.countCharFreq(s1)

        window_size = len(s1)
        win_start = 0
        win_end = win_start + window_size
        
        while win_end <= len(s2):
            window = s2[win_start:win_end]
            win_freq = self.countCharFreq(window)
            is_substring = True
            for c in s1:
                if c not in win_freq or char_to_freq[c] != win_freq[c]:
                    is_substring = False
                    break

            if is_substring:
                return True
            else:
                win_start += 1
                win_end += 1
        return False

    def countCharFreq(self, s: str) -> dict:
        hm = {}

        for c in s:
            if c in hm: hm[c] += 1
            else: hm[c] = 1

        return hm



