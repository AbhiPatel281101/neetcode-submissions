class MinStack:

    def __init__(self):
        self.Stake =  []
        self.minStake = []

    def push(self, val: int) -> None:
        self.Stake.append(val)
        val = min(val, self.minStake[-1] if self.minStake else val)
        self.minStake.append(val)

    def pop(self) -> None:
        self.Stake.pop()
        self.minStake.pop()

    def top(self) -> int:
        return self.Stake[-1]

    def getMin(self) -> int:
        return self.minStake[-1]
