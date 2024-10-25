from collections import defaultdict, deque
from math import ceil, floor, inf
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


def find_closest(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    if r == 0:
        return 0

    while l <= r:
        m = l + floor((r - l) / 2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return l


tc1 = [1, 2, 3, 4]
tc2 = [4, 10, 23, 25]
tc3 = [4, 11, 20, 23, 30]

print(tc1[find_closest(tc1, 2)])
print(tc2[find_closest(tc2, 16)])
print(tc3[find_closest(tc3, 15)])
print(tc3[find_closest(tc3, 0)])

# class Solution:
#     def run(self, piles: List[int], h: int) -> int:
#         min_rate = ceil(sum(piles) / h)
#         sorted_piles = sorted(piles)

#         # nearest to min rate
#         nearest_pile = find_closest(sorted_piles, min_rate)

#         # we haven't eaten any piles if we are at 0, so no off by one error here
#         piles_remaining = len(sorted_piles) - nearest_pile
#         hours_remaining = h - nearest_pile - 1

#         if piles_remaining == 0:
#             return min_rate

#         cur_pile = sorted_piles[nearest_pile]
#         finish_rate = ceil(cur_pile / min_rate)

#         if finish_rate == 1:
#             piles_remaining -= 1
#             hours_remaining -= 1
#         else:
#             hours_remaining += 1

#         if piles_remaining == 1:
#             return ceil(
#                 sorted_piles[nearest_pile] / (hours_remaining / piles_remaining)
#             )
#         best_case = hours_remaining - (finish_rate * piles_remaining)

#         test_pile = nearest_pile
#         test_hours_remaining = hours_remaining
#         test_piles_remaining = piles_remaining

#         while best_case >= 0 and len(piles) > test_pile and len(piles) > nearest_pile:
#             finish_rate = ceil(sorted_piles[test_pile] / min_rate)

#             if finish_rate == 1 or test_hours_remaining > 0:
#                 test_hours_remaining -= 1
#                 test_piles_remaining -= 1
#                 test_pile += 1
#             else:
#                 min_rate = sorted_piles[test_pile]
#                 test_hours_remaining = hours_remaining = hours_remaining - 1
#                 test_pile = nearest_pile = nearest_pile + 1
#                 test_piles_remaining = piles_remaining = piles_remaining - 1

#         while 0 > best_case and len(piles) > nearest_pile:
#             cur_pile = sorted_piles[nearest_pile]
#             test_piles_remaining = piles_remaining
#             test_hours_remaining = hours_remaining

#             min_rate = cur_pile

#             for i in range(nearest_pile, len(piles)):
#                 if 0 >= test_hours_remaining:
#                     break

#                 finish_rate = ceil(sorted_piles[i] / min_rate)
#                 best_case = test_hours_remaining - (finish_rate * test_piles_remaining)
#                 test_piles_remaining -= 1
#                 test_hours_remaining -= finish_rate

#                 if 0 > best_case:
#                     break

#             nearest_pile += 1
#             piles_remaining -= 1
#             hours_remaining -= 1
#         return min_rate


# class tests(unittest.TestCase):
#     # region setup/teardown
#     def setUp(self):
#         self.solution = Solution()

#     def tearDown(self):
#         self.solution = None

#     # endregion setup/teardown

#     def e(self, args, expected):
#         answer = self.solution.run(**args)
#         self.assertEqual(answer, expected)

#     # def test_double_hours(self):
#     #     self.e(
#     #         args=dict(piles=[1, 4, 3, 2], h=9),
#     #         expected=2,
#     #     )

#     # def test_minimal_hours(self):
#     #     self.e(
#     #         args=dict(piles=[25, 10, 23, 4], h=4),
#     #         expected=25,
#     #     )

#     # def test_one_more_hour(self):
#     #     self.e(
#     #         args=dict(piles=[30, 11, 23, 4, 20], h=6),
#     #         expected=23,
#     #     )

#     def test_big_end_more_time(self):
#         self.e(
#             args=dict(piles=[1, 1, 1, 999999999], h=10),
#             expected=142857143,
#         )


# if __name__ == "__main__":
#     unittest.main()

# optimal
# def minEatingSpeed(self, piles: List[int], h: int) -> int:
#     l, r = 1, max(piles)
#     res = r

#     while l <= r:
#         k = (l + r) // 2

#         totalTime = 0
#         for p in piles:
#             totalTime += math.ceil(float(p) / k)
#         if totalTime <= h:
#             res = k
#             r = k - 1
#         else:
#             l = k + 1
#     return res
