class MinStack:

    def __init__(self):
        self.st=[]
        self.minSt=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minSt:
            res=min(val,self.minSt[-1])
            self.minSt.append(res)
        else:
            self.minSt.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()
    
    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.minSt[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()