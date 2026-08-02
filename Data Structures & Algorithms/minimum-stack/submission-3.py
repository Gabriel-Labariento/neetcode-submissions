from sys import maxsize

class MinStack:

    def __init__(self):
        self.arr = []
        self.minstack = []
        self.currmin = maxsize

    def push(self, val: int) -> None:
        self.arr.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        
    def pop(self) -> None:
        self.arr.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.arr[len(self.arr) - 1]

    def getMin(self) -> int:
        return self.minstack[len(self.minstack) - 1]

        
