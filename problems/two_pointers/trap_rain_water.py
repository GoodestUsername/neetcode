from typing import List
import unittest


class Solution:
    def run(self, heights: List[int]) -> int:
        # my solution
        area = 0
        l = 0
        m = 1

        r = 0
        for i, num in enumerate(heights):
            if num >= heights[r]:
                r = i

        r = max(r, 2)

        while r > l and len(heights) > (r):
            if heights[l] == 0 or heights[l + 1] >= heights[l]:
                l += 1
                if l == m:
                    m = l + 1
                if r == m:
                    r = m + 1
            elif len(heights) > r + 1 and heights[r + 1] > heights[r]:
                r += 1
            elif m >= r:
                l = m
                m = l + 1
                r = m + 1
            elif heights[l] > heights[r] and heights[m] > heights[r]:
                if r + 1 == len(heights):
                    l += 1
                    m += 1
                else:
                    r += 1
            elif heights[l] > heights[m] and heights[r] > heights[m]:
                area += min(heights[l], heights[r]) - heights[m]
                m += 1
            else:
                l = m
                m += 1
        return area

    # def run(self, heights: List[int]) -> int:
    #     # optimal solution
    #     # for space complexity o(1)
    #     if not heights:
    #         return 0

    #     l, r = 0, len(heights) - 1
    #     leftMax, rightMax = heights[l], heights[r]
    #     res = 0
    #     while l < r:
    #         if rightMax > leftMax:
    #             l += 1
    #             leftMax = max(leftMax, heights[l])
    #             res += leftMax - heights[l]
    #         else:
    #             r -= 1
    #             rightMax = max(rightMax, heights[r])
    #             res += rightMax - heights[r]
    #     return res


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

    # def test_middles(self):
    #     self.e(args=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1], expected=9)

    # def test_right_end(self):
    #     self.e(args=[5, 4, 1, 2], expected=1)

    def test_big(self):
        self.e(
            args=[
                6,
                4,
                2,
                0,
                3,
                2,
                0,
                3,
                1,
                4,
                5,
                3,
                2,
                7,
                5,
                3,
                0,
                1,
                2,
                1,
                3,
                4,
                6,
                8,
                1,
                3,
            ],
            expected=83,
        )

    # def test_0_max_start(self):
    #     self.e(args=[0, 7, 1, 4, 6], expected=7)


if __name__ == "__main__":
    unittest.main()
