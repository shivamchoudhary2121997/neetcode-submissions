class MinStack:

    def __init__(self):
        self.list1 = []
        self.minval_list = []

    def push(self, val: int) -> None:
        if self.minval_list:
            minval = min(val, self.minval_list[-1])
        else:
            minval = val
        self.minval_list.append(minval)
        self.list1.append(val)

    def pop(self) -> None:
        self.minval_list.pop()
        self.list1.pop()

    def top(self) -> int:
        return self.list1[-1]

    def getMin(self) -> int:
        return self.minval_list[-1]
