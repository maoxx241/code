class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.index=0
        self.lst=[]
        self.size=size

    def next(self, val: int) -> float:
        if len(self.lst)<self.size:
            self.lst.append(val)
        else:
            if self.index<self.size-1:
                self.lst[self.index]=val
                self.index+=1
            elif self.index==self.size-1:
                self.lst[self.index]=val
                self.index=0
        return sum(self.lst)/len(self.lst)
            

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)