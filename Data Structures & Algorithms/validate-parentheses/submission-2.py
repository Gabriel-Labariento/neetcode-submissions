class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for b in s:
            if len(stack) == 0 and b in "}])":
                return False
            
            if b in "([{":
                stack.append(b)
            
            if b in ")}]":
                c = stack.pop()
                if b == ")" and c != "(":
                    return False
                if b == "}" and c != "{":
                    return False
                if b == "]" and c != "[":
                    return False
        
        if len(stack) == 0:
            return True
        return False
            