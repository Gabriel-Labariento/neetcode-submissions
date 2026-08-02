class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        lowered = s.lower()

        while i < j:
            while i < j and not (lowered[i].isalnum()):
                i += 1

            while j > i and not (lowered[j].isalnum()):
                j -= 1
        
            if lowered[i] != lowered[j]:
                return False

            i += 1
            j -= 1

        return True

