from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, heights: List[int]) -> int:
        currMax = 0
        l = 0
        r = len(heights) - 1

        while r > l:
            area = min(heights[l], heights[r]) * (r - l)
            currMax = max(currMax, area)

            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        return currMax


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def test_1(self):
        self.e(args=[1, 7, 2, 5, 4, 7, 3, 6], expected=36)

    def test_2(self):
        self.e(args=[2, 2, 2], expected=4)


if __name__ == "__main__":
    unittest.main()
