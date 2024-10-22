from math import inf
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, temperatures: List[int]) -> List[int]:
        total_days = len(temperatures)
        peak_temp_streaks = [0] * total_days
        stack = []

        for day in range(total_days):
            while len(stack) > 0 and temperatures[day] > stack[-1]["temperature"]:
                lower_temp_day = stack.pop()
                peak_temp_streaks[lower_temp_day["day"]] = day - lower_temp_day["day"]
            stack.append({"temperature": temperatures[day], "day": day})
        return peak_temp_streaks


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

    def test_random_walk(self):
        self.e(args=[30, 38, 30, 36, 35, 40, 28], expected=[1, 4, 1, 2, 1, 0, 0])

    def test_no_increasing(self):
        self.e(args=[22, 21, 20], expected=[0, 0, 0])


if __name__ == "__main__":
    unittest.main()

# first attempt (working)
# brute force version
# def run(self, temperatures: List[int]) -> List[int]:
#     total_days = len(temperatures)
#     peak_temp_streaks = [0] * total_days

#     for day in range(total_days):
#         for futureDay in range(day + 1, total_days):
#             if temperatures[futureDay] > temperatures[day]:
#                 peak_temp_streaks[day] = futureDay - day
#                 break
#     return peak_temp_streaks
