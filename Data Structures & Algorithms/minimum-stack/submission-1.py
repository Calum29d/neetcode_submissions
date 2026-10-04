class MinStack:

    def __init__(self):
        self.stack = [] # tuple (val, curMin)

    def push(self, val: int) -> None:
        if not self.stack or val < self.stack[-1][1]: # if stack empty or there is a new minimum
            self.stack.append((val, val))
        else:
            curMin = self.stack[-1][1]
            self.stack.append((val, curMin))
            

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
