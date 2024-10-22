from collections import defaultdict, deque
from math import ceil, inf
from typing import List
import unittest
import sys

sys.tracebacklimit = 0

# rules
# *

# part of the fleet if:
# *

# observations
# *

# strats
# *


class Solution:
    def run(self, heights: List[int]) -> int:
        rectangle_stack = []
        biggest = 0
        biggest_single = 0

        for l, height in enumerate(heights):
            biggest_single = max(biggest_single, height)

            if rectangle_stack and (
                rectangle_stack[-1] >= height or min_height >= height
            ):
                rectangle_stack.append(height)
                continue

            min_height = height

            for r in range(l + 1, len(heights)):
                min_height = min(min_height, heights[r])
                biggest = max(biggest, (r - l + 1) * min_height)

            rectangle_stack.append(height)

        if biggest_single > biggest:
            return biggest_single
        return biggest


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def test_multi(self):
        self.e(
            args=[3, 5, 5, 2, 5, 5, 6, 6, 4, 4, 1, 1, 2, 5, 5, 6, 6, 4, 1, 3],
            expected=24,
        )

    # def test_dup(self):
    #     self.e(args=[7, 1, 7, 2, 2, 4], expected=8)

    # def test_fleet_first_last(self):
    #     self.e(args=[1, 3, 7], expected=7)


if __name__ == "__main__":
    unittest.main()

# optimal solution
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         maxArea = 0
#         stack = []  # pair: (index, height)

#         for i, h in enumerate(heights):
#             start = i
#             while stack and stack[-1][1] > h:
#                 index, height = stack.pop()
#                 maxArea = max(maxArea, height * (i - index))
#                 start = index
#             stack.append((start, h))

#         for i, h in stack:
#             maxArea = max(maxArea, h * (len(heights) - i))
#         return maxArea
