from calendar import c
from collections import defaultdict, deque
from math import inf
from re import L
from typing import List
import unittest


class Solution:
    def run(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        if len(nums) == 1:
            return nums

        num_max_s = len(nums) - k + 1
        # k_max_arr = [0] * num_max_s
        k_max_map = [0] * num_max_s
        l = 0
        max_que = deque()
        # k: coord in nums
        # v: coord in stack

        cur_penultimate_max = 0
        cur_penultimate_maxx = 0
        popped = deque()

        cur_slot = 0
        cur_max = 0
        for r in range(k):
            if nums[r] > nums[k_max_map[0]]:
                cur_penultimate_max = k_max_map[0]
                k_max_map[0] = r
            elif nums[k_max_map[0]] > nums[r] and nums[r] > nums[cur_penultimate_max]:
                cur_penultimate_max = r
            while len(max_que) > 0 and nums[max_que[-1]] < nums[r]:

                # while len(max_que) > 0 and (nums[max_que[-1]] > nums[r] or max_que[0] > l):
                bopped = max_que.pop()

                if bopped >= l and r >= bopped:
                    popped.append(bopped)
                    # cur_penultimate_maxx = (
                    #     cur_penultimate_maxx
                    #     if nums[cur_penultimate_maxx] > nums[bopped]
                    #     else bopped
                    # )
            max_que.append(r)
            # if nums[r] > nums[k_max_map[0]]:
            #     k_max_map[0] = r
            # else:
            #     ordered_stack.append(nums[r])
            #     coord_map[r] = l

            # k_max_arr[0] = max(k_max_arr[0], nums[r])

        l += 1
        r += 1
        # the amount a stack solution needs to keep track of is k - 1 amount

        # removed isn't biggest(last item in k_max_arr)
        # if bigger than biggest? set as new item in k_max_arr
        # if smaller than biggest? biggest is repeated
        #   :
        # removed is biggest (last item in k_max_arr)
        # if bigger than biggest? set as new item in k_max_arr
        # if smaller than biggest?
        #   if bigger than semi_biggest? set as new item in k_max_arr
        #   if smaller than semi_biggest? set semi_biggest as new item in k_max_arr

        while len(nums) > r:
            while len(popped) > 0 and l > popped[0]:
                popped.popleft()

            while len(max_que) > 0 and l > max_que[0]:
                max_que.popleft()

            while len(max_que) > 0 and nums[max_que[-1]] < nums[r]:
                bopped = max_que.pop()

                if bopped >= l and r >= bopped:
                    popped.append(bopped)
                    # cur_penultimate_maxx = (
                    #     cur_penultimate_maxx
                    #     if nums[cur_penultimate_maxx] > nums[bopped]
                    #     and (cur_penultimate_maxx >= l and r >= cur_penultimate_maxx)
                    #     else bopped
                    # )
            max_que.append(r)

            cur_biggest_coord = k_max_map[l - 1]

            cur_num = nums[r]
            cur_biggest = nums[cur_biggest_coord]

            if cur_biggest_coord != l - 1:
                if cur_num >= cur_biggest:
                    cur_penultimate_maxx = cur_biggest_coord
                    k_max_map[l] = r
                else:
                    k_max_map[l] = cur_biggest_coord
                    if nums[r] > nums[cur_penultimate_maxx]:
                        cur_penultimate_maxx = r
            else:
                if cur_num >= cur_biggest:
                    k_max_map[l] = r
                else:
                    if cur_num > nums[max_que[0]]:
                        k_max_map[l] = r
                    else:
                        k_max_map[l] = max_que[0]
                    # if cur_num > nums[cur_penultimate_maxx]:
                    #     k_max_map[l] = r
                    # else:
                    #     k_max_map[l] = cur_penultimate_maxx
                    # cur_penultimate_max = cur_num

            r += 1
            l += 1
        return [nums[max_num] for max_num in k_max_map]


solution = Solution()
# print(solution.run(nums=[1, 2, 1, 0, 4, 2, 6], k=3))
# print(solution.run(nums=[7, 2, 4], k=2))
# print(solution.run(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

# print(solution.run(nums=[1, 3, 1, 2, 0, 5], k=3))
# print(solution.run(nums=[9, 10, 9, -7, -4, -8, 2, -6], k=5))
# print(solution.run(nums=[-7, -8, 7, 5, 7, 1, 6, 0], k=4))


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

    def test_medium(self):
        self.e(args=dict(nums=[1, 2, 1, 0, 4, 2, 6], k=3), expected=[2, 2, 4, 4, 6])

    def test_k_greater_than_half_len_nums(self):
        self.e(args=dict(nums=[7, 2, 4], k=2), expected=[7, 4])

    def test_very_long_small_k(self):
        self.e(
            args=dict(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3), expected=[3, 3, 5, 5, 6, 7]
        )

    def test_mid_sizes(self):
        self.e(args=dict(nums=[1, 3, 1, 2, 0, 5], k=3), expected=[3, 3, 2, 5])

    def test_very_long_both(self):
        self.e(
            args=dict(nums=[9, 10, 9, -7, -4, -8, 2, -6], k=5), expected=[10, 10, 9, 2]
        )

    def test_very_long_both_2(self):
        self.e(
            args=dict(nums=[-7, -8, 7, 5, 7, 1, 6, 0], k=4), expected=[7, 7, 7, 7, 7]
        )


if __name__ == "__main__":
    unittest.main()

# def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#     if k == 1:
#         return nums

#     if len(nums) == 1:
#         return nums

#     k_max_arr = []
#     l = 0
#     for r in range(k - 1, len(nums)):
#         k_max_arr.append(max(nums[l : r + 1]))
#         l += 1

#     return k_max_arr

# optimal
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         output = []
#         q = deque()  # index
#         l = r = 0

#         while r < len(nums):
#             while q and nums[q[-1]] < nums[r]:
#                 q.pop()
#             q.append(r)

#             if l > q[0]:
#                 q.popleft()

#             if (r + 1) >= k:
#                 output.append(nums[q[0]])
#                 l += 1
#             r += 1

#         return output
