# Definition of Interval:
from math import inf
from typing import List
import unittest


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# first attempt, O(n"2)
class Solution:
    def run(self, intervals: List[Interval]) -> bool:
        if 1 >= len(intervals):
            return True

        while intervals:
            cur = intervals.pop()
            for interval in intervals:
                if (
                    (cur.start >= interval.start and interval.end >= cur.end)
                    or (interval.start >= cur.start and cur.end >= interval.end)
                    or (cur.start >= interval.start and interval.end > cur.start)
                    or (cur.end > interval.start and interval.end >= cur.end)
                    or (interval.start >= cur.start and cur.end > interval.start)
                    or (interval.end > cur.start and cur.end >= interval.end)
                ):
                    return False

        return True


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

    # def test_conflicts(self):
    #     self.e(
    #         args=([Interval(0, 30), Interval(5, 10), Interval(15, 20)]),
    #         expected=False,
    #     )

    # def test_no_conflict(self):
    #     self.e(
    #         args=([Interval(5, 8), Interval(9, 15)]),
    #         expected=True,
    #     )

    # def test_big_list_some_conflicts(self):
    #     self.e(
    #         args=(
    #             [
    #                 Interval(1, 10),
    #                 Interval(9, 20),
    #                 Interval(19, 30),
    #                 Interval(29, 40),
    #                 Interval(39, 50),
    #             ]
    #         ),
    #         expected=False,
    #     )

    def test_no_conflict_matching_end_start(self):
        self.e(args=[Interval(0, 8), Interval(8, 10)], expected=True)


if __name__ == "__main__":
    unittest.main()

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# optimal solution
# class Solution:
#     def canAttendMeetings(self, intervals: List[Interval]) -> bool:
#         intervals.sort(key=lambda i: i.start)

#         for i in range(1, len(intervals)):
#             i1 = intervals[i - 1]
#             i2 = intervals[i]

#             if i1.end > i2.start:
#                 return False
#         return True
