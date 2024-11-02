from collections import defaultdict, deque
from math import ceil, floor, inf
from typing import List, Optional
import unittest
import sys

# sys.tracebacklimit = 0
# if even, find the furthest to the left median and the number greater than it
# get the distance of the first median by finding the position of the number closest to it in the next array,
# if it is found, add the position to the array1 len to get the position, otherwise the current position is the actual position

# cases
# no duplicate numbers
# [1, 2, 3] [4, 5, 6] continuous even numbers
# [1, 2]    [3, 4, 5] continuous odd, lower side smaller
# [1, 2, 3] [4, 5]    continuous odd, bigger side smaller
# [1, 3, 4] [2, 5, 6] not continuous even
# [1, 3, 4] [2, 5, 6] not continuous even

# duplicate numbers


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


def b_search_or_lower(
    nums: List[int], target: int, pos_tiebreaker: Optional[int] = None
) -> int:
    l, r = 0, len(nums) - 1
    if pos_tiebreaker != None and pos_tiebreaker > r:
        raise Exception("pos tiebreaker is must be less than or equal to arr size")

    if pos_tiebreaker != None and nums[pos_tiebreaker] == target:
        return pos_tiebreaker

    while l <= r:
        m = l + ((r - l) // 2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    if l == 0:
        return l
    return l - 1


def get_median(nums: List[int]) -> int:
    nums_len = len(nums)
    if nums_len == 0:
        return None

    if nums_len == 1:
        return nums[0]

    if (nums_len % 2) != 0:
        return nums[floor(nums_len / 2)]

    return (nums[floor((nums_len - 1) / 2)] + nums[floor(nums_len / 2)]) / 2


# should work after removing all off by one errors
# check if median of two arrays = median arr 1 + median arr 2
class Solution:
    def run(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        if nums1_len == 0 and nums2_len > 0:
            return get_median(nums2)
        elif nums2_len == 0 and nums1_len > 0:
            return get_median(nums1)
        elif nums1_len == 0 and nums2_len == 0:
            return 0

        if (nums1_len + nums2_len) % 2 != 0:
            return min(nums1[floor(nums1_len / 2)], nums2[floor(nums2_len / 2)])

        if nums1_len == nums2_len:
            if nums2[0] > nums1[-1]:
                return (nums1[-1] + nums2[0]) / 2
            if nums1[0] > nums2[-1]:
                return (nums1[0] + nums2[-1]) / 2
            if nums1[-1] == nums2[0] or nums2[-1] == nums1[0]:
                return nums1[-1]
        median_location = floor((nums1_len + nums2_len - 1) / 2)

        l1 = 0
        l2 = 0
        r1 = nums1_len - 1
        r2 = nums2_len - 1

        foundInArr1 = False
        foundInArr2 = False
        median_arr1_2 = -1
        median_arr2_2 = -1

        while r1 >= l1 and r2 >= l2 and not (foundInArr1 or foundInArr2):
            m1 = l1 + ((r1 - l1) // 2)
            m2 = l2 + ((r2 - l2) // 2)

            cur_num1 = nums1[m1]
            cur_num2 = nums2[m2]

            closest_loc_1 = b_search_or_lower(nums2, cur_num1, median_location - m2 - 1)
            closest_loc_2 = b_search_or_lower(nums1, cur_num2, median_location - m1 - 1)

            # right here is where it adds 1
            cur_arr_1_loc = m1 + closest_loc_1 + (1 if closest_loc_1 != 0 else 0)
            cur_arr_2_loc = m2 + closest_loc_2 + (1 if closest_loc_2 != 0 else 0)

            if median_location > cur_arr_1_loc:
                l1 = m1 + 1
            elif nums2[0] > cur_num1 and closest_loc_1 > 0:
                r1 = m1 - 1
            if median_location > cur_arr_2_loc:
                l2 = m2 + 1
            elif nums1[0] > cur_num2 and closest_loc_2 > 0:
                r2 = m2 - 1

            if cur_arr_1_loc == median_location:
                foundInArr1 = True
                print("case 1")
                median2_loc = closest_loc_1
                if (nums2_len - 1) > closest_loc_1 and cur_num1 == nums2[closest_loc_1]:
                    median2_loc = closest_loc_1 + 1

                if cur_num1 != nums1_len:
                    median_arr1_2 = nums2[median2_loc]
                else:
                    median_arr1_2 = min(nums2[median2_loc], nums1[m1])
            if cur_arr_1_loc == median_location:
                foundInArr2 = True
                print("case 2")
                median2_loc = closest_loc_1
                if (nums1_len - 1) > closest_loc_2 and cur_num2 == nums1[closest_loc_2]:
                    median2_loc = closest_loc_2 + 1

                if cur_num2 == nums2_len:
                    median_arr2_2 = nums1[median2_loc]
                else:
                    median_arr2_2 = min(nums1[median2_loc], nums2[m2])

        if foundInArr1 and median_arr1_2 >= median_arr2_2 and cur_num2 >= cur_num1:
            return (cur_num1 + median_arr1_2) / 2
        elif foundInArr2:
            return (cur_num2 + median_arr2_2) / 2
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

    def test_odd_small_left_small_right(self):
        self.e(
            args=dict(nums1=[1, 2], nums2=[3]),
            expected=2.0,
        )

    def test_odd_small_left_med_right(self):
        self.e(
            args=dict(nums1=[1, 2, 4, 5], nums2=[3]),
            expected=3.0,
        )

    def test_odd_small_right_small_left(self):
        self.e(
            args=dict(nums1=[3], nums2=[1, 2]),
            expected=2.0,
        )

    def test_odd_small_right_small_left(self):
        self.e(
            args=dict(nums1=[3], nums2=[1, 2, 4, 5]),
            expected=3.0,
        )

    def test_odd_med_right_med_left(self):
        self.e(
            args=dict(nums1=[1, 2, 3, 4], nums2=[3, 4, 5]),
            expected=3,
        )

    def test_equal_arrays_continues(self):
        self.e(
            args=dict(nums1=[1, 3], nums2=[2, 4]),
            expected=2.5,
        )

    def test_equal_arrays_continues(self):
        self.e(
            args=dict(nums1=[1, 2], nums2=[3, 4]),
            expected=2.5,
        )

    def test_equal_arrays_disjointed_1(self):
        self.e(
            args=dict(nums1=[2, 3], nums2=[2, 4]),
            expected=2.5,
        )

    def test_equal_arrays_disjointed_2(self):
        self.e(
            args=dict(nums1=[2, 3], nums2=[3, 4]),
            expected=3,
        )

    def test_equal_arrays_disjointed_3(self):
        self.e(
            args=dict(nums1=[1, 3], nums2=[2, 7]),
            expected=2.5,
        )

    def test_0_and_negatives_1(self):
        self.e(
            args=dict(nums1=[0, 0, 0, 0, 0], nums2=[-1, 0, 0, 0, 0, 0, 1]), expected=0
        )

    def test_equal_arrays_same_array(self):
        self.e(
            args=dict(nums1=[2, 2], nums2=[2, 2]),
            expected=2,
        )

    def test_empty_1(self):
        self.e(
            args=dict(nums1=[1, 2], nums2=[3, 4]),
            expected=2.5,
        )

    def test_empty_2(self):
        self.e(
            args=dict(nums1=[2, 3], nums2=[]),
            expected=2.5,
        )

    def test_empty_1(self):
        self.e(
            args=dict(nums1=[], nums2=[2, 3]),
            expected=2.5,
        )

    def test_empty_both(self):
        self.e(
            args=dict(nums1=[], nums2=[]),
            expected=0,
        )

    def test_mirror_arrays(self):
        self.e(
            args=dict(
                nums1=[2, 2, 4, 4],
                nums2=[
                    2,
                    2,
                    4,
                    4,
                ],
            ),
            expected=3,
        )


if __name__ == "__main__":
    unittest.main()
