class MinStack:

    def __init__(self):
        """
        Store minimum value we've encountered so far in another stack `minStack`
        """
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(
            val, self.minStack[-1] if self.minStack else val # compare insert value with the previous minimum value in minStack
        ))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
