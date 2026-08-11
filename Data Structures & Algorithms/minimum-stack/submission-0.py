class MinStack:

    def __init__(self):
        self.dq = deque()
        self.minDQ = deque() # storing the minimum for each point of index.

    def push(self, val: int) -> None:                
        self.dq.append(val)

        if len(self.minDQ) == 0:
            self.minDQ.append(val)
        elif self.minDQ[-1] < val:
            self.minDQ.append(self.minDQ[-1])
        else:
            self.minDQ.append(val)


    def pop(self) -> None:
        self.dq.pop()
        self.minDQ.pop()

    def top(self) -> int:
        return self.dq[-1]

    def getMin(self) -> int:
        return self.minDQ[-1]
        
