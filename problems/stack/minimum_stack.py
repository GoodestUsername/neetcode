from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


class tests(unittest.TestCase):
    def test(self):
        answer = []
        self.solution = MinStack()
        answer.append(self.solution.push(1))
        answer.append(self.solution.push(1))
        answer.append(self.solution.push(2))
        answer.append(self.solution.push(0))
        answer.append(self.solution.getMin())  # return 0
        answer.append(self.solution.pop())
        answer.append(self.solution.top())  # return 2
        answer.append(self.solution.getMin())
        self.assertEqual(
            answer,
            [None, None, None, None, 0, None, 2, 1],
        )


if __name__ == "__main__":
    unittest.main()
