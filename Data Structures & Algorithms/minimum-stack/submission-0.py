class MinStack:

    def __init__(self):
        # Maintains a tuple for each item of the stack.
        # (val, cur_min) as explained in the stack.push function
        self.stack = []


    def push(self, val: int) -> None:
        if self.stack:
            # Current item of stack will also have its own
            # current minimum value of the stack. We keep that
            # current minimum in the second element of a tuple.
            cur_min = min(val, self.stack[-1][1])
        else:
            cur_min = val

        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
