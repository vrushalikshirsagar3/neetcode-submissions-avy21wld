class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []
    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.min_st.append(val)
        else:
            self.st.append(val)
            if val < self.min_st[-1]:
                self.min_st.append(val)
            else:
                self.min_st.append(self.min_st[-1])

    def pop(self) -> None:
        if self.st:
            pop = self.st.pop()
            self.min_st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
