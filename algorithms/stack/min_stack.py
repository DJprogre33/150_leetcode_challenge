class Solution:
    """link to the problem: https://leetcode.com/problems/min-stack/"""
    class MinStack:

        def __init__(self):
            self.stack = []
            self.min = []

        def push(self, val: int) -> None:
            if not self.min or val < self.min[-1]:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
            self.stack.append(val)

        def pop(self) -> None:
            self.stack.pop()
            self.min.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min[-1]
