class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, val: int) -> None:
        minVal = self.getMin()
        if  minVal == None or val < minVal:
            minVal = val
        self.st.append([val,minVal])
        

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0] if self.st else None
        

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()