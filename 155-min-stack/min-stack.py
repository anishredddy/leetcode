class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min=val
        else:
            self.stack.append(val)
            self.min=min(self.min,val)

    def pop(self) -> None:
        p=self.stack.pop()
        if p==self.min and self.stack:
            self.min=min(self.stack)

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()