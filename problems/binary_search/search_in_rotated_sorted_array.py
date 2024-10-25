from collections import defaultdict, deque
from math import ceil, floor, inf
from typing import List
import unittest
import sys

# sys.tracebacklimit = 0


def b_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1


class Solution:
    def run(self, nums: List[int], target) -> int:
        l, r = 0, len(nums) - 1

        curr_min = inf

        while r >= l:
            m = l + ((r - l) // 2)
            curr_min = min(curr_min, nums[m])
            if nums[m] == target:
                return m
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l
            if nums[m] > target and not (nums[m] > nums[r] and not target > nums[r]):
                r = m - 1
            elif target > nums[m] or nums[m] > nums[r]:
                l = m + 1
        return -1


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

    # def test_min(self):
    #     self.e(
    #         args=dict(nums=[1], target=1),
    #         expected=0,
    #     )

    # def test_rot_2(self):
    #     self.e(
    #         args=dict(nums=[3, 5, 1], target=3),
    #         expected=0,
    #     )

    def test_rot_1(self):
        self.e(
            args=dict(nums=[5, 1, 3], target=5),
            expected=0,
        )

    # def test_rot_min_rot_1_contains(self):
    #     self.e(
    #         args=dict(nums=[3, 1], target=3),
    #         expected=0,
    #     )

    # def test_rot_4_found(self):
    #     self.e(
    #         args=dict(nums=[3, 4, 5, 6, 1, 2], target=1),
    #         expected=4,
    #     )

    # def test_rot_4_not_found(self):
    #     self.e(
    #         args=dict(nums=[3, 5, 6, 0, 1, 2], target=4),
    #         expected=-1,
    #     )


if __name__ == "__main__":
    unittest.main()

# optimal version, this one splits it up instead of trying to combine it like me
# more optimal since less comparisons, but still same time complexity "technically"

# def search(self, nums: List[int], target: int) -> int:
#     l, r = 0, len(nums) - 1

#     while l <= r:
#         mid = (l + r) // 2
#         if target == nums[mid]:
#             return mid

#         if nums[l] <= nums[mid]:
#             if target > nums[mid] or target < nums[l]:
#                 l = mid + 1
#             else:
#                 r = mid - 1

#         else:
#             if target < nums[mid] or target > nums[r]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#     return -1


# first solution, kinda cheating, should find better way
# def b_search(nums: List[int], target: int) -> int:
#     l, r = 0, len(nums) - 1

#     while l <= r:
#         m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
#         if nums[m] > target:
#             r = m - 1
#         elif nums[m] < target:
#             l = m + 1
#         else:
#             return m
#     return -1


# class Solution:
#     def run(self, nums: List[int], target) -> int:
#         nums_len = len(nums) - 1

#         l = 0
#         r = nums_len

#         cur_min = nums[l]
#         smallest = 0

#         while r >= l:
#             m = l + ((r - l) // 2)
#             left = m - 1
#             right = m + 1 if nums_len > m else 0

#             if nums[m] == target:
#                 return m
#             if nums[right] == target:
#                 return right
#             if nums[left] == target:
#                 return left

#             if nums[left] > nums[m] and nums[right] > nums[m]:  # case 2
#                 smallest = m
#             if nums[m] > nums[left] and nums[m] > nums[right]:  # case 1
#                 smallest = right

#             if nums[m] > cur_min:
#                 cur_min = nums[m]
#                 l = m + 1
#             else:
#                 r = m - 1

#         return b_search(nums[:-smallest] + nums[-smallest:], target)
