class MinStack:
    #going to have a tuple that contains the current minimum at the top and the tops value
    #(val, current minimum)
    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        #if the stack is empty then we know thats just going to be the minimum
        if not self.stack:
            self.stack.append((val,val)) #(val, currMin)
        else:
            currMin = min(self.stack[-1][1], val)
            self.stack.append((val, currMin))


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
